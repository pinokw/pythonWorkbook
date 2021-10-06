import os, sys, sqlite3
from sqlite3 import Error
fileDir = os.path.dirname(os.path.realpath('__file__'))


def create_connection():
    connection = None
    try:
        db_path=os.path.join(fileDir, 'data/adressbuch.db')
        connection = sqlite3.connect(db_path)
        print ()
        print("Connection to SQLite DB successful")
        # Tabelle erzeugen
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def delete_query(connection, id):
    table_name='person'
    #columns='*'
    where_conditions = 'id ' + '= ' + f"""{id}"""
    delete_row = '''
        DELETE
        FROM {}
        WHERE {}
    '''.format(table_name, where_conditions) 
    print (delete_row)
    return delete_row
    

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def start_delete(id):
    connection= create_connection()
    query= delete_query(connection, id)
    
    execute_query(connection, query)

if (__name__=='__main__'):
    pass



