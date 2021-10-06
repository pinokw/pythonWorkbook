import os, sys, sqlite3
from sqlite3 import Error
fileDir = os.path.dirname(os.path.realpath('__file__'))


def create_connection():
    connection = None
    try:
        dienstplan_db=os.path.join(fileDir, 'data/dienstplan.db')
        connection = sqlite3.connect(dienstplan_db)
        print("Connection to SQLite DB successful")
        # Tabelle erzeugen
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def delete_query(connection):
    delete_table = """
    DELETE 
    FROM 
        dienstplan
    WHERE 
        dienstplan.dp_date='2021-01-02 00:00:00 UTC'
    ;
    """
    return delete_table
    

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def start_delete():
    if os.path.exists(os.path.join(fileDir, 'data/dienstplan.db')):
        print("Die Datei existiert bereits")
        weiter=input(f'''Wollen Sie löschen ?
         (y/n)''')
        if weiter == 'y':
            pass
        else:
            sys.exit(0)
    connection= create_connection()
    table_query= delete_query(connection)
    execute_query(connection, table_query)

if (__name__=='__main__'):
    start_delete()



