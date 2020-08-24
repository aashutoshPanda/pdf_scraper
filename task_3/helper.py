from pathlib import Path
import textract
from nltk.tokenize import word_tokenize


def get_potential_stop_words():
    potential_stop_words = []
    wordfreq = {}
    total_files = 0
    for path in Path("task_3/profile_pdfs").iterdir():
        if path.is_file():
            if path.suffix != ".pdf":
                continue
            total_files += 1
            text = textract.process(path, method='pdfminer').decode('utf-8')
            list_of_words = word_tokenize(text)
            set_of_words = set(list_of_words)
            for word in set_of_words:
                if word not in wordfreq:
                    wordfreq[word] = 0
                wordfreq[word] += 1
    for key in wordfreq.keys():
        freq = wordfreq[key]
        if (freq > 0.85 * total_files):
            potential_stop_words.append(key)
    return (potential_stop_words)


if __name__ == "__main__":
    word_list = get_potential_stop_words()
    print(word_list)
