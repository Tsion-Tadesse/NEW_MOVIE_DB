import mysql.connector


mydb = mysql.connector.connect(host="localhost", user="root", password="password", database="MOVIE_THEATER_DB")


mycursor = mydb.cursor()

#mycursor.execute("Insert into account(fname, lname, user_id, password ) values (%s, %s, %s, %s)", ("Alex", "John", "alexJ", "1234"))

#mydb.commit()
mycursor.execute("SELECT * from Account")

for i in mycursor:
    print(i)

