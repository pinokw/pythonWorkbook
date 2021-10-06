import os, sys, sqlite3
from sqlite3 import Error
from typing import TYPE_CHECKING
fileDir = os.path.dirname(os.path.realpath('__file__'))
import csv


def create_connection():
    connection = None
    try:
        db_path=os.path.join(fileDir, 'data/adressbuch.db')
        connection = sqlite3.connect(db_path)
        #print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

def read_query(con, entry):
    table_name='person'
    columns='*'
    where_conditions = 'name ' + '= ' + f"""'{entry}'"""
    query = '''
        SELECT {}
        FROM {}
        WHERE {}
    '''.format(columns, table_name, where_conditions) 
    return query

def read_main(entry):
    con=create_connection()
    query=read_query(con, entry)
    result=execute_read_query(con, query)
    return result

def db_columns(table): 
    db_path=os.path.join(fileDir, 'data/adressbuch.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.execute(f'''select * from {table}''')
    columns = [description[0] for description in cursor.description]
    connection.close
    return columns

def rd_entries():
    db_path=os.path.join(fileDir, 'data/adressbuch.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    result=cursor.execute(f"SELECT name FROM person WHERE name <> 'none'")
    entries =[entry[0] for entry in result]
    connection.close
    return entries

def rd_ids():
    db_path=os.path.join(fileDir, 'data/adressbuch.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    result=cursor.execute("SELECT id FROM person WHERE name <> 'none'")
    entries =[entry[0] for entry in result]
    connection.close
    return entries


def check_entry(column, value):
    check_entry=False
    db_path=os.path.join(fileDir, 'data/adressbuch.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    check_condition=f"""{column}""" + ' = ' + f"""'{value}'"""
    print (check_condition)
    result=cursor.execute(f"""SELECT * FROM person WHERE {check_condition}""")
    connection.close
    entries=[entry[0] for entry in result]
    print (len(entries))
    if len(entries) > 0:
        check_entry=True
        return check_entry
    return check_entry

if (__name__=='__main__'):
    rd_entries()