from flask import Flask
from flask import render_template
import json
from flask import send_from_directory
from flask import request
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route("/")
def index_1():
    return "string"


@app.route("/show_student_information")
def show():
    # read file
    data = []
    with open("./data/student_information.txt",encoding='utf-8') as fin:
        is_first_line = True
        for line in fin:
            if is_first_line:
                is_first_line = False
                continue
            line = line[:-1]  # \n
            student_number, name, height = line.split("\t")
            data.append((student_number, name, height))
    return render_template("student_information.html", data=data)


@app.route("/show_student_information")
def show():
    # read file
    data = []
    with open("./data/student_information.json", encoding='utf-8') as fin:
        data = json.loads(fin.read())['data']

    return render_template("student_information_json.html", data=data)


@app.route("/download/<filepath>")
def index(filepath):
    return send_from_directory("./download_path", filename=filepath, as_attachment=True)


app.config['UPLOAD_FOLDER'] = 'upload_path/'


@app.route('/upload')
def upload_file():
    return render_template('upload.html')


@app.route('/upload_file', methods=['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        return 'file uploaded successfully'


if __name__ == "__main__":
    app.run(debug=True)
