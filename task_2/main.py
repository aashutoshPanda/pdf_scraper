import csv
from pathlib import Path
import textract


# field names of csv
fields = ['Name', 'Text']


# name of csv file
filename = "task_2/pdf_to_text.csv"
rows = []

for path in Path("task_2/profile_pdfs").iterdir():
    if path.is_file():
        if path.suffix != ".pdf":
            continue
        text = textract.process(path, method='pdfminer').decode('utf-8')
        rows.append([path.name, text])


# writing to csv file
with open(filename, 'w') as csvfile:

    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)
