from flask import *
from flask_mysqldb import *

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskerf'

mysql = MySQL(app)


@app.route('/')
def greet():
    return "Hello how are you for display data type in url /display"

@app.route('/display')
def renderDisplay():
    cur = mysql.connection.cursor()
    cur.execute("select * from register")

    data = cur.fetchone()
    cur.connection.commit()
    cur.close()

    return render_template("SendMultipleData.html" ,data=data)


if __name__ == '__main__':
    app.run(debug=True)