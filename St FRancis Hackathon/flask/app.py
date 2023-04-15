from flask import Flask, render_template, request, redirect, url_for, session, redirect, url_for
from flask_mysqldb import MySQL, MySQLdb
import MySQLdb.cursors
import re    

app = Flask(__name__)

app.secret_key = 'xyz123abc'
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='root123$'
app.config['MYSQL_DB']='donate'

mysql = MySQL(app)


@app.route('/')
def world():
    return render_template('world.html')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/volunteer', methods =['GET', 'POST'])
def volunteer():
    if request.method == 'POST' and request.form['name1'] and request.form['email'] and request.form['phone'] and request.form['address']:
        name= request.form['name1']
        email = request.form['email']
        phone = request.form['phone']
        address= request.form['address']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("INSERT into volunteer(name,email,phone,address) VALUES('{}','{}',{},'{}');".format(name,email,phone,address))
        mysql.connection.commit()
        user = cursor.fetchone()
        if user:
            session['loggedin'] = True
            session['id'] = user['id']
            session['name'] = user['name']
            session['email'] = user['email']
            session['phone'] = user['phone']
            session['address'] = user['address']
    return redirect(url_for('index'))
@app.route('/donation', methods =['GET', 'POST'])
def donation():
    if request.method == 'POST':
        name= request.form.get('name2')
        email = request.form.get('email2')
        amount= request.form.get('amount')
        print(name)
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(f"INSERT into donation(name,email,amount) VALUES('{name}','{email}','{amount}');")
        mysql.connection.commit()
        user = cursor.fetchone()
        if user:
            session['loggedin'] = True
            session['id'] = user['id']
            session['name'] = user['name']
            session['email'] = user['email']
            session['phone'] = user['phone']
            session['address'] = user['address']
    return redirect(url_for('index'))
    
    
if __name__ == "__main__":
    app.run(debug=True, port=8000)