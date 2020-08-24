
from helper import get_potential_stop_words

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')

# Un-comment to use the helper function to generate the extra-stop-words
# extra_stop_words = get_potential_stop_words()

extra_stop_words = ['Present', '-', 'of', 'Page', ')', 'months', ',', '·', 'Experience',
                    '1', 'LinkedIn', 'Skills', 'Top', 'Contact', 'Education', '(', 'at']


# set of stop words
stop_words = stopwords.words('english')
stop_words.extend(extra_stop_words)
stop_words = set(stop_words)

# function to remove stop_words from given text


def remove_stop_words(text):
    word_tokens = word_tokenize(text)
    filtered_sentence = []
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)
    return " ".join(filtered_sentence)


text = """ 

Contact

www.linkedin.com/in/sanskriti-
singhal-91093a145 (LinkedIn)

Sanskriti Singhal

SWE Intern'20 @Google || STEP Intern'19 @Google || Microsoft
Codess 2019 || DTU'21
New Delhi

Top Skills
Public Speaking
C
Java

Experience

D_CODER
Vice President
March 2019 - Present (1 year 6 months)

Microsoft
Codess
March 2019 - Present (1 year 6 months)

Google
Software Engineer Intern
May 2020 - Present (4 months)

Google
STEP Intern
May 2019 - July 2019 (3 months)
India

LaughGuru
Intern
December 2017 - January 2018 (2 months)
New Delhi Area, India

Education
Delhi Technological University
Bachelor of Technology, Computer Software Engineering · (2017 - 2021)

Delhi Public School Ghaziabad 
Class 12, PCM · (2004 - 2017)

Page 1 of 1

"""

filtered_text = remove_stop_words(text)
print(filtered_text)
