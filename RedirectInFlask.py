from flask import *

app = Flask(__name__)

@app.route('/rd')
def Redirect():
    return redirect(url_for("page"))

@app.route('/')
def page():
    return "Hello.redirection"


if __name__ == "__main__":
    app.run(debug=True)

