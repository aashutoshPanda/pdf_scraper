
import os
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.getcwd() + "/api/api_uploaded_files/"


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'file uploaded successfully'
    else:
        return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)
