import mysql.connector
from mysql.connector import Error

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="192.168.178.95",
            port= 5000,
            #unix_socket="run/mysqld/mysqld10.sock",
            user='root',
            passwd='tcVB73tRTu9J-*_', 
            database='mysql'
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

connection = create_connection()