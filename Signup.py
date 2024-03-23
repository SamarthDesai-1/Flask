from flask import *
from flask_mysqldb import *

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flasksignup'

mysql = MySQL(app)

@app.route('/')
def renderSignup():
    return render_template("Signup.html")

@app.route('/result' ,methods=['POST'])
def configResult():

    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name']
        mobile = request.form['mobile']
        password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute('insert into signup(Email ,Name ,Mobile ,Password) values(%s ,%s ,%s ,%s)' ,(email ,name ,mobile ,password))
        cur.connection.commit()
        cur.close()

        return "Insert records successfully"
    

if __name__ == '__main__':
    app.run(debug=True)
    
    