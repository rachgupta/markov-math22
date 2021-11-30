from sys import argv
import re
import nltk
from nltk import tokenize
from collections import Counter
import random
import glob
import os

#expects first command-line argument to be name of dir with files
current_path = os.getcwd()
new_path = current_path + "\\" + argv[1]
os.chdir(new_path)

#expects second command-line argument to be number of sentences
if(len(argv)>2):
    num_sentences = int(argv[2])
else:
    num_sentences = 5

#expects third command-line argument to be boolean indicating whether or not first word should be random
if(len(argv)>3):
    random_first = bool(argv[3])
else:
    random_first = False

#expects fourth command-line argument to be list of first_words
if(len(argv)>4):
    literal = argv[4].replace("[","")
    literal = literal.replace("]","")
    list_of_first_words = [c for c in literal.split(",")]

#expects fifth command-line argument to be max number of words in a sentence
if(len(argv)>5):
    max_words = int(argv[5])
else:
    max_words = 100

all_txt_files = glob.glob('*.txt')
# Initialize an dictionary for all the txts
texts = {}

# Populates a dictionary of full texts
for i in range(len(all_txt_files)):
    text = open(all_txt_files[i])
    texts[all_txt_files[i]] = text.read()
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
        all_sentences.append([w.lower() for w in sentence_words])
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

def validate_rows(matrix):
    numRight = 0
    numWrong = 0
    for i in matrix:
        count = 0
        for j in matrix[i]:
            count = count + matrix[i][j]
        if round(count,4) == 1:
            numRight = numRight + 1
        else:
            print(count)
            numWrong = numWrong + 1
    print("right: " + str(numRight))
    print("wrong: " + str(numWrong))

def roulette(words):
    random.seed()
    selection = random.random() #floating between 0 and 1
    #plug weights and candidates into random choice function
    weights = []
    candidates = []
    for candidate in words.keys():
        weights.append(words[candidate])
        candidates.append(candidate)
    if(sum(weights)==0):
        return "."
    choice = random.choices(candidates, weights=weights, k=1)
    return choice[0]


def generate_random_sentence(matrix, first_word,max_words):
    sentence = first_word.capitalize()
    current_word = first_word
    for i in range(max_words):
        #generate next word in sentence
        current_word = roulette(matrix[current_word])
        #check if word is end of sentence punctuation
        sentence = sentence + " " + current_word
        # if so break loop
        # if not continue
        if(current_word=="."):
            return sentence
    return sentence
for i in range(num_sentences):
    print(generate_random_sentence(matrix, list_of_first_words[i],max_words))
    print("")
    #print("done")