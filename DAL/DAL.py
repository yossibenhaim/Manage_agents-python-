import mysql.connector

myDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="eagleeyedb"
)
mycursor = myDB.cursor()

def send_query(query):
    mycursor.execute(query)
    myDB.commit()