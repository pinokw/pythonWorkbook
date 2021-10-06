import os, sys, sqlite3
from sqlite3 import Error
fileDir = os.path.dirname(os.path.realpath('__file__'))

def create_connection():
    connection = None
    try:
        db_path=os.path.join(fileDir, 'data/adressbuch.db')
        connection = sqlite3.connect(db_path)
        print("Connection to SQLite DB successful")       
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection


def execute_update_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        cursor.close()
    except Error as e:
        print(f"The error '{e}' occurred")

def query_write(connection, person):
    cursor = connection.cursor()
    data = [{'vorname':person[0], 
        'name': person[1], 
        'gebdat': person[2], 
        'street': person[3],
        'plz': person[4],
        'city': person[5],
        }]
    cursor.executemany("""
        INSERT INTO
            person
            (vorname, name, gebdat, street, plz, city)
        VALUES
            (:vorname, :name, :gebdat, :street, :plz, :city)""", data)
    connection.commit()
    print('Der Datensatz wurde erfolgreich geändert')
    
def write(person):
    connection=create_connection()
    query_write(connection, person)


if (__name__=='__main__'):
    pass
