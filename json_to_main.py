import spacy
import nltk.classify.util
from nltk.corpus import stopwords
from nltk.classify import NaiveBayesClassifier
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.feature_extraction.text import CountVectorizer
import os
import errno
# from sklearn.cross_validation import cross_val_score
from classify import pos_tag, word_dep
from nltk.tokenize import RegexpTokenizer
import sys
import json

sys.path.append('/Users/Work/Documents/College/Senior/Senior Seminar/Main/virtualenv/lib/python3.6/site-packages')

def sort(input_dictionary):

    #for each business
    for business in input_dictionary:
        #get list containing all reviews
        review_list = input_dictionary[business]
        #replace n symbols
        #print("This is the review list " + str(review_list))
        review_list = {x.replace('\n', '') for x in review_list}
        #print("This is after replacement " + str(review_list))
        tokenizer = RegexpTokenizer("[\w']+")
        full = []
        tagged_list = []
        word_dep_list = []

        #tokenize the words in each individual review within the full list of reviews
        for x in review_list:

            # useful_words = tokenizer.tokenize(x)
            # full.append(useful_words)
            full.append(x)

            # tags = pos_tag(x)
            # tagged_list.append(tags)
            #
            # word_dep_labeled = word_dep(x)
            # word_dep_list.append(word_dep_labeled)


        print(business)
        filename = str("raw_output/" + business + ".txt")

        #begin writing of text
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "a+") as f:
            temp_dict = dict()
            temp_dict.update({'raw_review': full})
            # temp_dict.update({'tagged_review': tagged_list})
            # temp_dict.update({"word_dep_review": word_dep_list})
            #print(temp_dict)

            #cleaned_words = pos_tag(full)
            #https://stackabuse.com/reading-and-writing-lists-to-a-file-in-python/
            json.dump(temp_dict, f)

            f.close()
            print("file closed")




