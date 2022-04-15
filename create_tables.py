import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="password", database="MOVIE_THEATER_DB")


mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE Account(fname varchar(20), lname varchar(20), user_id varchar(20) PRIMARY KEY, password varchar(8) )")
#mycursor.execute("CREATE TABLE Movie(title varchar(20) PRIMARY KEY, rating varchar(20), duration DATETIME, release_date DATETIME, summary varchar(200) )")
#mycursor.execute("CREATE TABLE Employee(Employee_id INT PRIMARY KEY, fname varchar(20), lname varchar(20))")