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

#expects third command-line argument to be list of first_words
if(len(argv)>3):
    literal = argv[3].replace("[","")
    literal = literal.replace("]","")
    list_of_first_words = [c for c in literal.split(",")]

#expects fourth command-line argument to be max number of words in a sentence
if(len(argv)>4):
    max_words = int(argv[4])
else:
    max_words = 500

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
        #remove punctuation
        sentence = re.sub(r'[^\w\s]', '', sentence)
        sentence = re.sub(r'\n', '', sentence)
        #split sentence into list of words
        sentence_words = re.split(' ', sentence)
        #make each word lowercase and add it to the matrix
        for word in sentence_words:
            matrix[word.lower()] = {}
        #add to greater list of sentences
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


#helper function that we used to validate that our matrix has rows adding up to 1
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


#uses probability from given dictionary of words to randomly choose a word
def roulette(words):
    random.seed()
    #plug weights and candidates into random choice function
    weights = []
    candidates = []
    for candidate in words.keys():
        weights.append(words[candidate])
        candidates.append(candidate)
    
    #if the word doesn't have anything following it in any instance, return end of sentence punctuation
    if(sum(weights)==0):
        return "."
    choice = random.choices(candidates, weights=weights, k=1)
    return choice[0]


def markov_chain(stochastic, first_word,max_words):
    sentence = first_word.capitalize()
    # get the probabilities for that first word (x1)
    running_vector = stochastic[first_word]
    #initialize the current_word variable with the first word given
    current_word = first_word
    #repeat for each word in the sentence
    for i in range(max_words):
        #use the weights to choose a new word
        current_word = roulette(running_vector)
        #end the sentence if the new word indicates a natural end to the sentence
        if(current_word=="."):
            return sentence + "."
        #if not, add the new sentence
        sentence = sentence + " " + current_word
        #Xn = P * X(n-1)
        #update Xn using stochastic matrix and current X(n-1)
        running_vector = matrix_mult(stochastic, list(running_vector.values()))
    return sentence

#generate random sentence using just the word before and the stochastic matrix
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
    #print(markov_chain(matrix, list_of_first_words[i],max_words))
    print("")

#helper function to do matrix multiplication
def matrix_mult(matrix, vector):
    #matrix will be dictionary of dictionaries
    #vector will be list
    new_dict = {}
    row_names = list(matrix.keys())
    for i in range(len(row_names)):
        num = 0
        column_names = list(matrix[row_names[i]].keys())
        for j in range(len(column_names)):
            num = num + vector[j]*matrix[row_names[i]][column_names[j]]
        new_dict[row_names[i]] = num
    return new_dict