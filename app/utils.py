
from pathlib import Path
import textract

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')

extra_stop_words = ['Present', '-', 'of', 'Page', ')', 'months', ',', '·', 'Experience',
                    '1', 'LinkedIn', 'Skills', 'Top', 'Contact', 'Education', '(', 'at']

# set of stop words
stop_words = stopwords.words('english')
stop_words.extend(extra_stop_words)
stop_words = set(stop_words)


def remove_stop_words(text):
    word_tokens = word_tokenize(text)
    filtered_sentence = []
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)
    return " ".join(filtered_sentence)


def get_text(path):
    if path.is_file():
        if path.suffix != ".pdf":
            raise Exception("not pdf")

        # print("got ", path.name, " in utils")
        text = textract.process(path, method='pdfminer').decode('utf-8')
        return text
        # return "random form utils"


def get_text_without_stop_words(path):
    if path.is_file():
        if path.suffix != ".pdf":
            raise Exception("not pdf")
        text = textract.process(path, method='pdfminer').decode('utf-8')
        filtered_text = remove_stop_words(text)
        return filtered_text
