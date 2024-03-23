from flask import *

app = Flask(__name__)

@app.route('/Display/<string:str>')
def displayAtHome(str):
    return render_template("Home.html" ,data=str)

if __name__ == '__main__':
    app.run(debug=True)