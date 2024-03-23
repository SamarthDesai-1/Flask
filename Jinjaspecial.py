from flask import *

app = Flask(__name__)

@app.route('/')
def greet():
    name="Samarth R S Desai"
    error="Wrong Email ID and PASSWORD"
    return render_template("jinja.html" ,error=error)

if __name__ == '__main__':
    app.run(debug=True)