from flask import *

app = Flask(__name__)
app.secret_key = "SECRET_KEY"

@app.route('/')
def renderLogin():
    return render_template('Login.html')

@app.route('/result' ,methods=['POST'])
def generateSession():
    if request.method == 'POST':
        session['name'] = request.form['email']
        name = session['name']
        return render_template("Home.html" ,name=name)

@app.route('/logout' ,methods=['POST'])
def renderLogout():
    session.clear()
    return redirect(url_for('renderLogin'))

@app.route('/erf' ,methods=['POST'])
def renderERFTemplate():
    return render_template('ERF.html')

if __name__ == '__main__':
    app.run(debug=True)    
    
    