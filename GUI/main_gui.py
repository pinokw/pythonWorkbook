import tkinter as Tk
import os, sys
from tkinter import ttk
from tkinter import font
import tkinter.messagebox
fileDir = os.path.dirname(os.path.realpath('__file__'))
sys.path.append(fileDir)
from parse_writeDB.db_operation import analyze_db
from parse_writeDB.db_operation import dyn_query
import gui_calc
from sqlite3 import Error
from openpyxl import Workbook

# Main Frame
root=Tk.Tk()
root.geometry('700x800')
data_columns=analyze_db.db_columns('dienstplan')
lbl_header=Tk.Label(root, text="Dienstplan Viewer 1.0", padx=5, pady=5)
lbl_header.grid(column=0, row=0)
#lbl_header.pack()
#Frame Auswahl
fr_auswahl=Tk.LabelFrame(root, text="Abfrage-Auswahl", padx=5, pady=5)
#fr_auswahl.pack()
fr_auswahl.grid(column=0, row=2, padx=5, pady=5)
fr_check=Tk.LabelFrame(root, text="Aktion", padx=5, pady=5)
fr_check.grid(column=0,  row=3, padx=5, columnspan=3, pady=5)
#fr_check.pack()
#Frame ausgabe
fr_ausgabe=Tk.LabelFrame(root, text="Ausgabe", padx=5, pady=5)
fr_ausgabe.grid(column=0, columnspan=3, row=4, padx=5, pady=5)
#fr_ausgabe.pack()


def add_cmb(int_adds):
    global cmb_value
    cmb_value=int_adds+1
    print (cmb_value)
    globals()[('%s%i' % ('cmb_column',int_adds))]=ttk.Combobox(fr_auswahl, values=data_columns)
    globals()[('%s%i' % ('cmb_column', int_adds))].set("Auswahl")
    globals()[('%s%i' % ('cmb_oper',int_adds))]=ttk.Combobox(fr_auswahl, values=("<", "=", ">"))
    globals()[('%s%i' % ('cmb_oper', int_adds))].set("Auswahl")
    globals()[('%s%i' % ('cmb_value',int_adds))]= Tk.Text(fr_auswahl, font=("Arial", 16), height=1, width=15, bd=5, highlightcolor='grey', relief='raised')
    globals()[('%s%i' % ('cmb_column',int_adds))].grid(column=0, row=int_adds)
    globals()[('%s%i' % ('cmb_oper',int_adds))].grid(column=1, row=int_adds)
    globals()[('%s%i' % ('cmb_value',int_adds))].grid(column=2, row=int_adds)
    cmd_addCmb=Tk.Button(fr_auswahl, text='Add Auswahl', command=lambda: add_cmb(int_adds+1))
    cmd_addCmb.grid(column=1, row=int_adds+1)
    cmd_searchDB=Tk.Button(fr_check, text='Suche in Datenbank', command=lambda: request2db(cmb_value))
    cmd_searchDB.grid(column=0, row=0)
    radio_noex=Tk.Radiobutton(fr_check, text='No Export', variable=rb, value=1)
    radio_noex.grid(column=1, row=0)
    radio_ex=Tk.Radiobutton(fr_check, text='Export to XLS', variable=rb, value=2)
    radio_ex.grid(column=2, row=0)

def request2db(int_adds):
    filter=[]
    for i in range (int_adds):      
        if (globals()[('%s%i' % ('cmb_column', i))].get() == "Auswahl") \
            or (globals()[('%s%i' % ('cmb_oper', i))].get() == "Auswahl") \
            or (globals()[('%s%i' % ('cmb_value', i))].get('1.0', 'end') == ""):
            continue
        column=(globals()[('%s%i' % ('cmb_column', i))].get())
        oper=(globals()[('%s%i' % ('cmb_oper', i))].get())
        value=(globals()[('%s%i' % ('cmb_value', i))].get('1.0', 'end'))
        value=value.rstrip()
        # Anfragen zu einem dictionary zusammenstellen
        value=gui_calc.value_check(column, value)
        if value=="EXIT":
            break
        #print (value)
        filter.append({'column':column, 'op':oper, 'value':value})
        print (filter)
    try: 
        # dictionary an dyn_query übergeben und abfragen
        result=dyn_query.main_dynquery(filter)  
        #print (result) 
        ausgabe(result)
    except Error as e:
        #Tk.messagebox.WARNING(title="Fehler", message=e)
        print(f"The error '{e}' occurred")
        
# Ergebnis ausgeben im Viewer
def ausgabe(result):
    liste.delete(0, Tk.END)
    for x, entry in enumerate(result):
        liste.insert(x, entry)
    message=f''' Es wurden 
    {len(result)} Einträge mit den Suchkriterien gefunden'''
    Tk.messagebox.showinfo(title="Suchergebnis", message=message)
    export_choice=rb.get()
    if export_choice==2:
        print_xls(result)
        Tk.messagebox.showinfo(title="Export erfolgreich", message="Das Ergebnis wurde in " + fileDir +"/data/export.xlsx ausgegeben.")
    else:
        return

def print_xls(result):
    xlsfile=os.path.join(fileDir, 'data/export.xlsx')
    wb=Workbook()
    sheet = wb.active
    headerdata=data_columns
    sheet.append(headerdata)
    for pilot in result:
        sheet.append(pilot)
    freezy=sheet['Y2']
    sheet.freeze_panes=freezy
    sheet.auto_filter.ref = "A1:Y1"
    wb.save(xlsfile)
   
#Widgets Auswahl1
rb=Tk.IntVar()
rb.set(0)
cmb_value=2
for i in range (cmb_value):
    globals()[('%s%i' % ('cmb_column',i))]=ttk.Combobox(fr_auswahl, values=data_columns)
    globals()[('%s%i' % ('cmb_column', i))].set("Auswahl")
    globals()[('%s%i' % ('cmb_oper',i))]=ttk.Combobox(fr_auswahl, values=("<", "=", ">"))
    globals()[('%s%i' % ('cmb_oper', i))].set("Auswahl")
    globals()[('%s%i' % ('cmb_value',i))]= Tk.Text(fr_auswahl, font=("Arial", 16), height=1, width=15, bd=5, highlightcolor='grey', relief='raised')
    globals()[('%s%i' % ('cmb_column',i))].grid(column=0, row=i)
    globals()[('%s%i' % ('cmb_oper',i))].grid(column=1, row=i)
    globals()[('%s%i' % ('cmb_value',i))].grid(column=2, row=i)
#Widgets Check
cmd_addCmb=Tk.Button(fr_auswahl, text='Add Auswahl', command=lambda: add_cmb(cmb_value))
cmd_addCmb.grid(column=1, row=i+1)
cmd_searchDB=Tk.Button(fr_check, text='Suche in Datenbank', command=lambda: request2db(cmb_value))
cmd_searchDB.grid(column=0, row=0)
radio_noex=Tk.Radiobutton(fr_check, text='No Export', variable=rb, value=1)
radio_noex.grid(column=1, row=0)
radio_ex=Tk.Radiobutton(fr_check, text='Export to XLS', variable=rb, value=2)
radio_ex.grid(column=2, row=0)
#Widgets Ausgabe
liste=Tk.Listbox(fr_ausgabe, width=65, height=30, relief='raised')
liste.grid(row=0, column=0, padx=5, pady=5 )


root.mainloop()