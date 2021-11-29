from sys import argv
import re
import nltk
from nltk import tokenize

# Initialize an dictionary for arg inputs
texts = {}

# Populates a dictionary of full texts
for i in range(len(argv) - 1):
    text = open(argv[i + 1])
    texts[argv[i + 1]] = text.read()
    text.close()


#main dictionary
matrix = {}
for file in texts:
    text = texts[file]
    #split into sentences (list of sentences)
    sentences = tokenize.sent_tokenize(text)
    for sentence in sentences:
        #remove punctuation and add to matrix
        sentence = re.sub(r'[^\w\s]', '', sentence)
        sentence = re.sub(r'\n', '', sentence)
        sentence_words = re.split(' ', sentence)
        for word in sentence_words:
            matrix[word.lower()] = []