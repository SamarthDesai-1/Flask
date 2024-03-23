from flask import *

app = Flask(__name__)

@app.route('/')
def loadHomeHTML():
    return render_template('Home.html')

if __name__ == '__main__':
    app.run(debug=True)

    