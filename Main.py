from flask import *
from flask_mysqldb import *
import os

app = Flask(__name__)


UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.secret_key = "SECRET_KEY"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flasksignup'

mysql = MySQL(app)

@app.route('/home')
def home():
    name = session['name']
    return render_template("Home.html" ,name=name)

@app.route('/login')
def login():
    return render_template("Login.html")
    
    
@app.route('/')
def renderLogin(): 
    return render_template("Login.html")

@app.route('/resultlogin' ,methods=['POST'])
def result():
    email = request.form['email']
    password = request.form['password']

    if email == 'Admin@gmail.com' and password == '101010':
        session['ADMIN'] = email
        return redirect(url_for('admin'))

    cur = mysql.connection.cursor()

    users = cur.execute("select * from signup where Email = %s" ,(email,))
    data = cur.fetchone()

    cur.connection.commit()
    cur.close()
    
    if users >= 1:
        if email == data[1] and password == data[4]:
            session['name'] = data[2]
            name = session['name']
            return render_template("Home.html" ,name=name)

        else:
            error = "Please retype email and password"
            return render_template("Login.html" ,error=error)
            
    elif users == 0:
        return render_template("Signup.html")

    return render_template("Login.html")

@app.route('/login' ,methods=['POST'])
def renderLogout():
    session.clear()
    return render_template("Login.html")


@app.route('/resultsignup' ,methods=['POST'])
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

        return render_template("Login.html")
    
    
@app.route('/rendererf' ,methods=['POST'])
def renderERF():
    return render_template("ERF.html")


@app.route('/resulterf' ,methods=['POST'])
def configERF():
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_DB'] = 'flaskerf'

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

        file = request.files['file']
        if file:

            FILENAME = file.filename

            filename = os.path.join(app.config['UPLOAD_FOLDER'] ,file.filename)
            file.save(filename)
            cur = mysql.connection.cursor()
            cur.execute("insert into register(First ,Middle ,Last ,Address ,Salary ,Gender ,DOB ,Grades ,Age ,Files) values(%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s)" ,(first ,middle ,last ,address ,salary ,gender ,dob ,grades ,age ,FILENAME))
            cur.connection.commit()
            cur.close()

            return redirect(url_for("home"))
    else:
        return render_template("ERF.html")


@app.route('/admin')
def admin():
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'flaskerf'

    if 'ADMIN' in session:     
        cur = mysql.connection.cursor()
        cur.execute("select * from register")
        userDetails = cur.fetchall()
        cur.connection.commit()
        cur.close()
        return render_template("Admin.html" ,userDetails=userDetails)
    else:
        return redirect(url_for('login'))

@app.route('/display_image/<filename>')
def display_image(filename):
    return redirect(url_for('static' ,filename=f'uploads/{filename}'))


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


@app.route('/display_data/<string:id>')
def renderUpdate(id):
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'flaskerf'

    cur = mysql.connection.cursor()
    cur.execute("select * from register where ID = %s" ,(id,))

    userDetails = cur.fetchone()
    cur.connection.commit()
    cur.close()
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

    file = request.files['file']
    if file:
        FILENAME = file.filename
        filename = os.path.join(app.config['UPLOAD_FOLDER'] ,file.filename)
        file.save(filename)

    cur = mysql.connection.cursor()
    cur.execute("update register set First = %s ,Middle = %s ,Last = %s ,Address = %s ,Salary = %s ,Gender = %s ,DOB = %s ,Grades = %s ,Age = %s ,Files = %s where ID = %s" ,(first ,middle ,last ,address ,salary ,gender ,dob ,grades ,age ,FILENAME , id,))
    cur.connection.commit()
    cur.close()
    
    return redirect(url_for("admin"))

@app.route('/delete/<string:id>')
def deleteData(id):
    cur = mysql.connection.cursor()
    cur.execute("delete from register where ID = %s" ,(id,))
    cur.connection.commit()
    cur.close()

    return redirect(url_for("admin"))

if __name__ == '__main__':
    app.run(debug=True)
    
