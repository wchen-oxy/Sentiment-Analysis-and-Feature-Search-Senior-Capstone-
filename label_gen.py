import spacy
import nltk.classify.util
from nltk.corpus import stopwords
from nltk.classify import NaiveBayesClassifier
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.cross_validation import cross_val_score
from nltk.tokenize import RegexpTokenizer
import sys
import json

sys.path.append('/Users/Work/Documents/College/Senior/Senior Seminar/Main/virtualenv/lib/python3.6/site-packages')

def Pos_Sort(input):
    target = open('positive1.txt', "a+")
    pos = []
    full = []
    file = open(input, "r")
    for line in file:
        if "\t1\n" in line:
            pos.append(line.lower())
    pos = {x.replace('\t1\n', '') for x in pos}
    for review in pos:
        tokenizer = RegexpTokenizer("[\w']+")
        useful_words = tokenizer.tokenize(review)
        # useful_words = tokenizer.tokenize(useful_words)
        full.append(useful_words)
        for x in useful_words:
            target.write(str(x) + " ")
        target.write("\n")

    target.close()
    file.close()


def Neg_Sort(input):
    target = open('negative1.txt', "a+")
    neg = []
    full = []
    file = open(input, "r")
    for line in file:
        if "\t0\n" in line:
            neg.append(line.lower())
    neg = {x.replace('\t0\n', '') for x in neg}
    for review in neg:
        tokenizer = RegexpTokenizer("[\w']+")
        useful_words = tokenizer.tokenize(review)
        # useful_words = tokenizer.tokenize(useful_words)
        full.append(useful_words)
        for x in useful_words:
            target.write(str(x) + " ")
        target.write("\n")

    target.close()
    file.close()

def punctuation_check(string):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    if string in punctuations:
        return True


def punctuation(string):
    # punctuation marks
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    # traverse the given string and if any punctuation
    # marks occur replace it with null
    if string in punctuations:
        string = string.replace(string, "")
        return string
    else:
        # Print string without punctuation
        return string

if __name__ == '__main__':
    file = "sentiment_labelled_sentences/yelp_labelled.txt"
    Pos_Sort(file)
    Neg_Sort(file)
    # neg = Neg_Sort(file)

# SortAndTokenize(input)


file = open('things.txt', "a")

file.close