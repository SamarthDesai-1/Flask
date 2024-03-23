from flask import *
from flask_mysqldb import *

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskerf'

mysql = MySQL(app)

# @app.route('/')
# def renderAdmin():
#     cur = mysql.connection.cursor()
#     cur.execute("select * from register")
#     userDetails = cur.fetchall()
#     cur.connection.commit()
#     cur.close()
#     return render_template("Admin.html" ,userDetails=userDetails)


@app.route('/display/<string:id>')
def renderUpdate(id):
    cur = mysql.connection.cursor()
    cur.execute("select * from register where ID = %s" ,(id,))

    userDetails = cur.fetchone()
    return render_template("Update.html" ,userDetails=userDetails)

@app.route('/saveddata/<string:id>' ,methods=['POST'])
def savedData(id):
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
    cur.execute("update register set First = %s ,Middle = %s ,Last = %s ,Address = %s ,Salary = %s ,Gender = %s ,DOB = %s ,Grades = %s ,Age = %s where ID = %s" ,(first ,middle ,last ,address ,salary ,gender ,dob ,grades ,age ,id,))
    cur.connection.commit()
    cur.close()
    
    return render_template("Home.html")

@app.route('/delete/<string:id>')
def deleteData(id):
    cur = mysql.connection.cursor()
    cur.execute("delete from register where ID = %s" ,(id,))
    cur.connection.commit()
    cur.close()

    cur = mysql.connection.cursor()
    cur.execute("select * from register")
    userDetails = cur.fetchall()
    cur.connection.commit()
    cur.close()
    return render_template("Admin.html" ,userDetails=userDetails)

@app.route('/ascending')
def sortAscending():
    cur = mysql.connection.cursor()
    cur.execute("select * from register order by Salary ASC")
    userDetails = cur.fetchall()
    cur.connection.commit()
    cur.close()

    return render_template("Admin.html" ,userDetails=userDetails)

@app.route('/descending')
def sortdescending():
    cur = mysql.connection.cursor()
    cur.execute("select * from register order by Salary DESC")
    userDetails = cur.fetchall()
    cur.connection.commit()
    cur.close()

    return render_template("Admin.html" ,userDetails=userDetails)

if __name__ == '__main__':
    app.run(debug=True)
