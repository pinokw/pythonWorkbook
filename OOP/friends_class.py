from tkinter import *

class Friend:

    species='Pauls Freunde' # class attribute (gilt für die gesamte klasse)

    def __init__(self, name, vn, adress, TelNr): # initiatior of instance (gilt nicht für die gesamte klasse)
        self.name=name
        self.vn=vn
        self.adress=adress
        self.tel=TelNr

root = Tk()
root.title('Titel')
root.geometry('500x700')
global freunde_liste
freunde_liste=[]

def berechnen():
    name=input_name.get()
    vn=input_vn.get()
    adress=input_adr.get()
    TelNr=input_TelNr.get()
    # Erstelle Class-Object
    freund=Friend(name, vn, adress, TelNr)
    # Speichere Class-Object in Liste
    freunde_liste.append(freund)
    input_name.delete(0, "end")
    input_vn.delete(0, "end")
    input_adr.delete(0, "end")
    input_TelNr.delete(0, "end")

def show_friends():
    freunde=""
    for x, item in enumerate(freunde_liste):
        # print(item.name)
        freunde += str(x) + f'''. 
        Vorname:    {item.vn} 
        Nachname:   {item.name} 
        Adresse:    {item.adress}  
        Telefon:    {item.tel}  
        ''' + "\n"
    out_txt.delete('1.0', END)
    out_txt.insert(END, freunde)

#Frame
input_frame=LabelFrame(root, text="Input").pack()
output_frame=LabelFrame(root, text='Output')
my_scrollbar=Scrollbar(output_frame, orient=VERTICAL)
#Name
label1=Label(input_frame, text="Name ").pack(padx=5, pady=5)
input_name=Entry(input_frame)
input_name.pack()
#Vorname
label2=Label(input_frame, text="Vorname ").pack(padx=5, pady=5)
input_vn=Entry(input_frame)
input_vn.pack()
#Adresse
label2=Label(input_frame, text="Adresse ").pack(padx=5, pady=5)
input_adr=Entry(input_frame, width=20)
input_adr.pack()
#Telefonnummer
label2=Label(input_frame, text="Telefonnummer ").pack(padx=5, pady=5)
input_TelNr=Entry(input_frame)
input_TelNr.pack()
button=Button(input_frame, text="Add Friend", command=berechnen).pack()
button=Button(input_frame, text="Show Friends", command=show_friends).pack()
#Output
out_txt=Text(output_frame, width=200, height=50, yscrollcommand=my_scrollbar.set)
# Configure Scrollbar
my_scrollbar.config(command=out_txt.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)
output_frame.pack(padx=10, pady=10)
out_txt.pack(padx=5, pady=5)


root.mainloop()
