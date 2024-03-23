from flask import *
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['ALLOWED_EXTENSIONS'] = {'png' ,'jpeg' ,'jpg'}
# app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 # 50 KB limit

@app.route('/')
def renderUpload():
    return render_template("upload.html")

@app.route('/upload' ,methods=['POST'])
def uploadDOCS():
    if request.method == 'POST':
        file = request.files['file']
        # if file and allowed_file(file.filename):
        if file:
            filename = os.path.join(app.config['UPLOAD_FOLDER'] ,file.filename)
            file.save(filename)
            return "File uploaded Successfully"
        else:
            return "No files are selected yet"
    return "Invalid Request"

if __name__ == '__main__':
    app.run(debug=True)

