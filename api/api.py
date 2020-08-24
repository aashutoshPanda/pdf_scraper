
import os
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.getcwd() + "/api/api_uploaded_files/"


@app.route('/text', methods=['GET', 'POST'])
def text():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(
            app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))

        return jsonify(
            pdf_name=secure_filename(f.filename),
            text="random garbage"
        )

    return render_template('index.html')


@app.route('/text_without_stopwords', methods=['GET', 'POST'])
def text_without_stopwords():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(
            app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))

        return jsonify(
            pdf_name=secure_filename(f.filename),
            text="random garbage"
        )

    return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
