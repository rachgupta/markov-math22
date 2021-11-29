from sys import argv
import re
import nltk
from nltk import tokenize
from collections import Counter

# Initialize an dictionary for arg inputs
texts = {}

# Populates a dictionary of full texts
for i in range(len(argv) - 1):
    text = open(argv[i + 1])
    texts[argv[i + 1]] = text.read()
    text.close()


#main dictionary
matrix = {}
all_sentences = []
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
            matrix[word.lower()] = {}
        all_sentences.append(sentence_words)
for word in matrix:
    #finds all the words that follow a given word in the matrix
    following_words = []
    for sentence in all_sentences:
        for i in range(len(sentence)-1):
            if sentence[i]==word:
                following_words.append(sentence[i+1])
    #counts the number of instances of words following that word
    count = Counter(following_words)
    #inputs probabilities for every possible word following that word into the matrix
    for key in matrix:
        instances = count[key]
        if(len(following_words)>0):
            matrix[word][key] = instances/len(following_words)
        else:
            matrix[word][key] = 0
print(matrix)