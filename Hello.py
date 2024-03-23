from flask import *

app = Flask(__name__)

@app.route('/')
def greet():
    return "Hello Flask Developer"

if __name__ == '__main__':
    app.run(debug=True)
