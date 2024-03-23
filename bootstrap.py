from flask import *

app = Flask(__name__)

@app.route('/')
def render():
    return render_template("boot.html")

if __name__ == '__main__':
    app.run(debug=True)