from flask import *
from flask_mysqldb import *

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskdemo'

mysql = MySQL(app)

@app.route('/')
def renderLogin():
    return render_template('Login.html')

@app.route('/result' ,methods=['POST'])
def configResult():
    
    username = request.form['email']
    password = request.form['password']
    
    cur = mysql.connection.cursor()
    cur.execute("insert into flask_db(Email ,Password) value(%s ,%s)" ,(username ,password))
    cur.connection.commit()
    cur.close()

    return ""

@app.route('/user')
def renderUsers():
    cur = mysql.connection.cursor()
    users = cur.execute("select * from flask_db")
    if users > 0:
        usersDetails = cur.fetchall()
        
        return render_template("users.html" ,usersDetails=usersDetails)


if __name__ == '__main__':
    app.run(debug=True)
    

