import mysql.connector

def connect():
    mydb = mysql.connector.connect(
        host="sql6.freesqldatabase.com",
        user="sql6419099",
        password="SiuSJtwaGg",
        database="sql6419099"
        ) 
    return mydb