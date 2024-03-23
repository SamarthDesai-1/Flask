from flask import *
from flask_mysqldb import *

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskerf'

mysql = MySQL(app)

@app.route('/')
def manual():
    message = '''For create database write /BASE/Database Name in url and for create table write TABLE in url'''
    return message

@app.route('/base/<name>')
def createBase(name):
    databasename = name
    
    cur = mysql.connection.cursor()
    cur.execute(f"create database {databasename}")
    cur.connection.commit()
    cur.close()

    return "Database created successfully"

@app.route('/signup')
def createTable():
    cur = mysql.connection.cursor()
    cur.execute("create table signup (ID int primary key AUTO_INCREMENT ,Email varchar(30) ,Name varchar(20) ,Mobile varchar(10) ,Password varchar(10))")
    cur.connection.commit()
    cur.close()

    return "Table created successfully"


@app.route('/erf')
def createTableERF():
    cur = mysql.connection.cursor()
    cur.execute('''create table register(ID int primary key AUTO_INCREMENT ,First varchar(20) ,Middle varchar(20) ,Last varchar(20) ,Address varchar(100) ,Salary numeric ,Gender varchar(7) ,DOB date ,Grades numeric ,Age numeric ,Filename varchar(30))''')
    cur.connection.commit()
    cur.close()
    
    return "Table created successfully"

    
if __name__ == '__main__':
    app.run(debug=True)

