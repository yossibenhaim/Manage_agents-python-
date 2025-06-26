import mysql.connector

myDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="eagleeyedb"
)
my_cursor = myDB.cursor()

def send_query(query,value):
    value = eval(repr(value))
    my_cursor.execute(query,value)
    myDB.commit()

def get_query(query,value = ""):
    my_cursor.execute(query,value)
    my_result = my_cursor.fetchall()
    for i in my_result:
        print(i)