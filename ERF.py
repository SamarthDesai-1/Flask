from flask import *
from flask_mysqldb import *

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_DB'] = 'flaskerf'

mysql = MySQL(app)

@app.route('/')
def renderERF():
    return render_template("ERF.html")

@app.route('/result' ,methods=['POST'])
def configERF():

    if request.method == 'POST':
        first = request.form['firstname']
        middle = request.form['middlename']
        last = request.form['lastname']
        address = request.form['address']
        salary = request.form['salary']
        gender = request.form['gender']
        dob = request.form['dateofbirth']
        grades = request.form['grades']
        age = request.form['age']

        cur = mysql.connection.cursor()
        cur.execute("insert into register(First ,Middle ,Last ,Address ,Salary ,Gender ,DOB ,Grades ,Age) values(%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s)" ,(first ,middle ,last ,address ,salary ,gender ,dob ,grades ,age))
        cur.connection.commit()
        cur.close()

        return render_template("Login.html")

if __name__ == '__main__':
    app.run(debug=True)

