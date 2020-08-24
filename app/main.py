
from flask import jsonify
import os
from pathlib import Path
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, jsonify
from utils import get_text, get_text_without_stop_words

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.getcwd(
) + "pdf_scraper/app/api_uploaded_files/"


# route to extract text from given pdf file
@app.route('/text', methods=['GET', 'POST'])
def text():
    if request.method == 'POST':
        # saving the recived pdf file to upload folder
        f = request.files['file']
        f.save(os.path.join(
            app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))

        # making pathlib 'Path' object to send to helper function
        path = Path(
            os.getcwd() + "pdf_scraper/app/api_uploaded_files/" + f.filename)

        if (not path.is_file()) or (path.suffix != ".pdf"):
            return jsonify(error=400, text="Invalid Request"), 400

        text = get_text(path)

        return jsonify(
            pdf_name=secure_filename(f.filename),
            text=text
        )

    return render_template('index.html')

# route to extract text(without stop-words) from given pdf file


@app.route('/text_without_stopwords', methods=['GET', 'POST'])
def text_without_stopwords():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(
            app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))

        # making pathlib 'Path' object to send to helper function
        path = Path(
            os.getcwd() + "pdf_scraper/app/api_uploaded_files/" + f.filename)
        if (not path.is_file()) or (path.suffix != ".pdf"):
            return jsonify(error=400, text="Invalid Request"), 400

        text_without_stop_words = get_text_without_stop_words(path)

        return jsonify(
            pdf_name=secure_filename(f.filename),
            text_without_stop_words=text_without_stop_words
        )

    return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
