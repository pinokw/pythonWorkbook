import os, sys, sqlite3
from sqlite3 import Error
fileDir = os.path.dirname(os.path.realpath('__file__'))

def create_connection():
    connection = None
    try:
        dienstplan_db=os.path.join(fileDir, 'data/dienstplan.db')
        connection = sqlite3.connect(dienstplan_db)
        print("Connection to SQLite DB successful")
        # gen_query(connection, filter)
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

def gen_query(connection, filters):
    table_name='dienstplan'
    columns='*'
    where_conditions = [f['column'] +' '+ f['op'] +' '+ f['value'] for f in filters] # Aus Filter-dict wird eine Liste mit allen Filterinhalten gebaut
    query = ''' 
        SELECT {}
        FROM {}
        WHERE {}
    '''.format(', '.join(columns), table_name, ' AND '.join(where_conditions)) # Listen werden in STRING verwandelt
    print(query.__repr__())
    return query

def main_dynquery(filter):
    connection=create_connection()
    query=gen_query(connection, filter)
    result=execute_query(connection, query)
    return result 


if (__name__=='__main__'):
    pass
    #main_dynquery([{'column': 'station', 'op': '=', 'value': "'FRA'"}, {'column': 'bzw', 'op': '>', 'value': '80'}])