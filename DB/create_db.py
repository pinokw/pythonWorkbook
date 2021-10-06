import os, sys, sqlite3
from sqlite3 import Error
fileDir = os.path.dirname(os.path.realpath('__file__'))


def create_connection():
    #db_name=input("Wie soll der Name der DB lauten?")
    connection = None
    try:
        db_path=os.path.join(fileDir, 'data/adressbuch.db')
        connection = sqlite3.connect(db_path)
        print("Connection to SQLite DB successful")
        # Tabelle erzeugen
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def create_query(connection):
    create_table = """
    CREATE TABLE IF NOT EXISTS person(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        vorname TEXT,
        gebdat INTEGER, 
        street TEXT,
        plz INTEGER,
        city TEXT 
    );
    """
    return create_table
    

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def start_creation():
    if os.path.exists(os.path.join(fileDir, 'data/adressbuch.db')):
        print("Die Datei existiert bereits")
        weiter=input(f'''Wollen Sie die bestehende Datenbank löschen 
        und eine neue erstellen?
        WARNUNG: ALLE BESTEHENDEN DATEN WERDEN GELÖSCHT! (y/n)''')
        if weiter == 'y':
            pass
        else:
            sys.exit(0)
    connection= create_connection()
    table_query= create_query(connection)
    execute_query(connection, table_query)

if (__name__=='__main__'):
    start_creation()



