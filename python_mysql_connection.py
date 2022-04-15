import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="password")

print(mydb)

if(mydb):
    print("connection happened")
else:
    print("no connection")