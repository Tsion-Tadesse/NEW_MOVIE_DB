from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
import mysql.connector
from datetime import datetime
from datetime import datetime
# from flask_mysqldb import MySQL
#import MySQLdb.cursors
import re
app = Flask(__name__, template_folder='Template')

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/movie')
def movie():
    return render_template('movie.html')

@app.route('/ticket')
def ticket():
    return render_template('ticket.html')

@app.route('/search')
def search():
    return render_template('search.html')
@app.route('/account_registeration')
def account_reg():
    return render_template('account_registeration.html')
@app.route('/reset_pwd')
def reset_password():
    return render_template('reset_pwd.html')
@app.route('/Add_movie')
def add_movies():
    return render_template('Add_movie.html')
@app.route('/admin')
def admin():
    return render_template('admin.html')
@app.route('/update_movie')
def update_movies():
    return render_template('update_movie.html')
@app.route('/add_ticket')
def add_ticks():
    return render_template('add_ticket.html')
@app.route('/delete_movie')
def del_movie():
    return render_template('delete_movie.html')
mydb = mysql.connector.connect(host = "localhost",user = "root",password = "password", database="MOVIE_THEATER_DB")
mycursor=mydb.cursor()
@app.route('/search', methods=['POST', 'GET'])
def search_result():
    if request.method=='POST':
        title = request.form['title']
        mycursor.execute("SELECT * FROM Movie WHERE title='"+title+"'")
        res = mycursor.fetchall()

        mydb.commit()

    # mycursor.close()
    return render_template('search.html', res=res)
@app.route('/Add_movie', methods=['POST', 'GET'])
def add_movie():

    if request.method=='POST':
        title = request.form['title']
        duration = request.form['Duration']
        rating = request.form['Rating']
        summary = request.form['Summary']
        genres = request.form['Genres']
        date = request.form['date']
        month = request.form['month']
        year = request.form['year']
        # release_date = request.form['release_date'] had hard time taking user input as a date
        mycursor.execute("Insert into Movie(title, duration, rating, summary, genres, date, month, year) values(%s, %s,%s,%s, %s,%s,%s, %s)",
                         (title, int(duration), rating, summary, genres,  int(date), int(month), int(year)))
        mydb.commit()
    return "Added a movie sucessfully!"

@app.route('/movie', methods=['POST', 'GET'])
def display_all_movie():
    if request.method == 'POST':
        mycursor.execute("SELECT * FROM Movie")
        show = mycursor.fetchall()

    return render_template('movie.html', show=show)

@app.route('/update_movie', methods=['POST', 'GET'])
def update_movie():
    if request.method=='POST':
        title = request.form['title']
        duration = request.form['Duration']
        rating = request.form['Rating']
        summary = request.form['Summary']
        genres = request.form['Genres']
        date = request.form['date']
        month = request.form['month']
        year = request.form['year']
        mycursor.execute("SELECT * FROM Movie WHERE title='" + title + "'")
        movie_exsist = mycursor.fetchall()
        if movie_exsist:
            mycursor.execute("UPDATE Movie SET title='" + title + "', Duration='"+duration+"', Rating='"+rating+"', Summary='"+summary+"',Genres='"+genres+"', date='"+date+"', month='"+month+"', year='"+year+"'  ")

        else:
            print("Movie doesn't exsist!")
        mydb.commit()
    return "Movie updated sucessfully!"
@app.route('/delete_movie', methods=['POST', 'GET'] )
def delete_movie():
    if request.method == 'POST':
        title = request.form['title']
        mycursor.execute("DELETE FROM Movie WHERE title='"+title+"'")
        mycursor.fetchall()
        mydb.commit()
    return "The Movie Deleted sucessfully!!"
@app.route('/add_ticket', methods=['POST', 'GET'])
def add_ticket():
    if request.method=='POST':
        Ticket_number = request.form['Ticket_number']
        Price = request.form['Price']
        num_available_ticket = request.form['num_available_ticket']
        movie_name = request.form['movie_name']
        mycursor.execute("Insert into Ticket(Ticket_number, Price, num_available_ticket, movie_name) values(%s, %s,%s,%s)",
                         (int(Ticket_number), int(Price),  int(num_available_ticket), movie_name ))
        mydb.commit()
    return "Added a ticket sucessfully!"
#@app.route('/', method=['POST', 'GET'])
# def display_by_catagoty()
#     if request.method == 'POST':
#
#     return render_template('\search', dip=dip)

# secrete key for protection but optional
# app.secret_key = '1234'
#
# # Enter your database connection details below
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'password'
# app.config['MYSQL_DB'] = 'MOVIE_THEATER_DB'
#
# # Intialize MySQL
# mysql = MySQL(app)
#
# @app.route('/login')
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     message = ''
#     if request.method == 'POST' and 'user_id' in request.form and 'password' in request.form :
#         user_id = request.form['user_id']
#         password = request.form['password']
#
#         cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#         cursor.execute('select * from Account WHERE user_id= %s AND password=%s', (user_id, password,) )
#
#         account = cursor.fetchone()
#         if account:
#             session['loggedin'] = True
#             session['user_id'] = account['user_id']
#             message = 'logged in successfully'
#         else:
#             message = "wrong username/password/no account been detected! "
#     return render_template('login.html', message = message)
# @app.route('/logout')
# def logout():
#     session.pop('loggedin', None)
#     session.pop('user_id', None)
#     return redirect(url_for('login'))
# @app.route('/account_registration', methods=['GET', 'POST'])
# def register():
#     message=''
#     if request.method == 'POST' and 'fname' in request.form and 'lname' in request.form and 'user_id' in request.form and 'password' in request.form:
#         fname = request.form['fname']
#         lname = request.form['lname']
#         user_id = request.form['user_id']
#         password = request.form['password']
#         cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#         cursor.execute('SELECT * FROM Account WHERE user_id = %s', (user_id, ))
#         account = cursor.fetchone()
#         if account:
#             message = 'There is an account under user name, instead try to log int'
#         else:
#             cursor.execute('INSERT INTO MOVIE_THEATER_DB.Account VALUES(%s, %s, %s, %s)', (fname, lname, user_id, password, ))
#             mysql.connection.commit()
#             message = "You have registered!"
#     elif request.method == 'POST':
#         message = "Fill out the account register form"
#     return render_template('account_registration.html', message=message)

# @app.route('/profile')
# def profile():
#     return render_template('profile.html')
if __name__ == '__main__':
    app.run(
        port=8000,
        debug=True
    )
