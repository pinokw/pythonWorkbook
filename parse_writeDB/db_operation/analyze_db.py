import sqlite3, os
from openpyxl import Workbook
from parse_writeDB.db_operation  import dyn_query
fileDir = os.path.dirname(os.path.realpath('__file__'))

def db_columns(table): 
    dienstplan_db=os.path.join(fileDir, 'data/dienstplan.db')
    connection = sqlite3.connect(dienstplan_db)
    cursor = connection.execute(f'''select * from {table}''')
    columns = [description[0] for description in cursor.description]
    connection.close
    return columns

def filter_menu(columns):
    filter=[]
    while True:
        print('*'*30)
        print ('Sie können aus folgenden Angaben wählen')
        for wert, column in enumerate(columns):
            print (wert, column)
        print ('*'*30)
        x=len(columns)-1
        arg_int=int(input(f'''Nach welchem Argument wollen Sie filtern? 
        Sie haben die Wahl von 0 - {x} '''))
        column_select=columns[arg_int]
        value_input=input(f'''Welchen wert soll der Ausdruck {column_select} annehmen ? ''')
        operator_input=(input(f''' Soll der Ausdruck {column_select} größer (>) 
        kleiner (<) oder gleich (=) dem beschriebenen Wert {value_input} sein? '''))      
        filter.append({'column':column_select, 'op':operator_input, 'value':value_input})
        if input("Wollen Sie noch einen Parameter untersuchen (y wenn ja)?")=="y": 
            pass
        else:
            break
    return filter

def analyse (analy_result, filter):
    for x, entry in enumerate(analy_result):
        print(x, entry)
    analy_nmbr=len(analy_result)
    print (f'''
        Es konnten {analy_nmbr} Datensätze gefunden werden.''')
    if input("Möchten Sie die Datensätze in einer Datei ausgeben (y) ?")=="y":
        print_xls(analy_result)

def print_xls(result):
    xlsfile=os.path.join(fileDir, 'data/export.xlsx')
    wb=Workbook()
    sheet = wb.active
    headerdata=xls_columns('dienstplan')
    sheet.append(headerdata)
    for pilot in result:
        sheet.append(pilot)
    freezy=sheet['Y2']
    sheet.freeze_panes=freezy
    sheet.auto_filter.ref = "A1:Y1"
    wb.save(xlsfile)

def xls_columns(table): 
    dienstplan_db=os.path.join(fileDir, 'data/dienstplan.db')
    connection = sqlite3.connect(dienstplan_db)
    cursor = connection.execute(f'''select * from {table}''')
    columns = [description[0] for description in cursor.description]
    connection.close
    return columns

def main():
    columns=db_columns('dienstplan')
    filter= filter_menu(columns)
    print (filter)
    if input("Möchten Sie die Analyse starten?") == 'y':
        analy_result=dyn_query.main_dynquery(filter)
        analyse(analy_result, filter)
    else:
        exit

# check DB columns
if (__name__=='__main__'):
    pass
    
