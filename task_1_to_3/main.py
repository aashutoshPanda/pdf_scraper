
import csv
from pathlib import Path
import textract

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')
set(stopwords.words('english'))


# set of stop words
stop_words = set(stopwords.words('english'))


# field names
fields = ['Name', 'Text', 'Text-without-stopwords']


# name of csv file
filename = "task_1_to_3/pdf_to_text.csv"
rows = []


def remove_stop_words(text):
    word_tokens = word_tokenize(text)
    filtered_sentence = []
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)
    return " ".join(filtered_sentence)


for path in Path("task_1_to_3/profile_pdfs").iterdir():
    if path.is_file():
        if path.suffix != ".pdf":
            continue
        text = textract.process(path, method='pdfminer').decode('utf-8')
        filtered_text = remove_stop_words(text)

        # print(filtered_text)
        rows.append([path.name, text, filtered_text])


# writing to csv file
with open(filename, 'w') as csvfile:

    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)
