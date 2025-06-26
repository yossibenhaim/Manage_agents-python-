import mysql.connector

myDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="eagleeyedb"
)
mycursor = myDB.cursor()

def send_query(query,value):
    mycursor.execute(query,value)
    myDB.commit()