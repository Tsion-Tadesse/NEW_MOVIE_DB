import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="password", database="MOVIE_THEATER_DB")


mycursor = mydb.cursor()