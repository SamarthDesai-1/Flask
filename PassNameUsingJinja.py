from flask import *

app = Flask(__name__)

@app.route('/user')
def renderName():
    name = "samarth desai"
    return render_template('index.html' ,username=name)

if __name__ == '__main__':
    app.run(debug=True)