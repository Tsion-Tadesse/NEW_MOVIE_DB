from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)

# secrete key for protection but optional
app.secret_key = '1234'

# Enter your database connection details below
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'MOVIE_THEATER_DB'

# Intialize MySQL
mysql = MySQL(app)

@app.route('/login')
@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST' and 'user_id' in request.form and 'password' in request.form :
        user_id = request.form['user_id']
        password = request.form['password']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('select * from Account WHERE user_id= %s AND password=%s', (user_id, password,) )

        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['user_id'] = account['user_id']
            message = 'logged in successfully'
        else:
            message = "wrong username/password/no account been detected! "
    return render_template('login.html', message = message)
@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('user_id', None)
    return redirect(url_for('login'))
@app.route('/account_registration', methods=['GET', 'POST'])
def register():
    message=''
    if request.method == 'POST' and 'fname' in request.form and 'lname' in request.form and 'user_id' in request.form and 'password' in request.form:
        fname = request.form['fname']
        lname = request.form['lname']
        user_id = request.form['user_id']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM Account WHERE user_id = %s', (user_id, ))
        account = cursor.fetchone()
        if account:
            message = 'There is an account under user name, instead try to log int'
        else:
            cursor.execute('INSERT INTO MOVIE_THEATER_DB.Account VALUES(%s, %s, %s, %s)', (fname, lname, user_id, password, ))
            mysql.connection.commit()
            message = "You have registered!"
    elif request.method == 'POST':
        message = "Fill out the account register form"
    return render_template('account_registration.html', message=message)
