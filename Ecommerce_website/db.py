

import mysql.connector

dbconnect = mysql.connector.connect(host="localhost", port=3306, user="root", password="",database="clothifyy_db")

mycursor = dbconnect.cursor()

print(dbconnect)

if not dbconnect:
    print("Error!")
else:
    print("Connected to the server")
mycursor.execute("SHOW DATABASES;")
for i in mycursor:
    print(i)

mycursor.execute("DESCRIBE category_1_car;")
for i in mycursor:
    print(i)

mycursor.execute("SELECT * from category_1_car")
for i in mycursor:
    print(i)