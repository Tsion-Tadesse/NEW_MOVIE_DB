import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="password")

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE MOVIE_THEATER_DB")

#mycursor.execute("Show database")

#for db in mycursor:
#    print(db)