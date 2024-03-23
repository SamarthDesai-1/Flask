from flask import *

app = Flask(__name__)

@app.route('/')
def renderLogin():
    return render_template("login.html")

@app.route('/Display' ,methods=['POST'])
def displayToHome():
    if request.method == 'POST':   
        data = request.form['name']
        return render_template("Home.html" ,data=data)

if __name__ == '__main__':
    app.run(debug=True)