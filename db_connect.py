import mysql.connector

def connect():
    mydb = mysql.connector.connect(
        host="10.10.96.4",
        user="root",
        password="Bimal@24625",
        database="users"
        ) 
    return mydb