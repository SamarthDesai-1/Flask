from flask import *

app = Flask(__name__)

@app.route('/')
def renderTemplate():
    return render_template("nav.html")

@app.route('/display' ,methods=['POST'])
def display():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        salary = request.form['salary']
        list = []
        list.append(name)
        list.append(age)
        list.append(salary)

        return render_template("display.html" ,data=list)


if __name__ == '__main__':
    app.run(debug=True)

