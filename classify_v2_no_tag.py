import os
from classify import pos_tag, word_dep
from nltk.tokenize import RegexpTokenizer
import sys
import spacy
import json
from textblob import TextBlob


def file_create(file_address):
    print("start")
    file = open(file_address, "r")
    temp = ""

    for x in file:
        parsed_json = json.loads(str(x))
        raw_review = parsed_json['raw_review']
        # print(raw_review)
        filename = str("cleaned/" + file_address)

        # begin writing of text
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "a+") as f:
            temp_dict = dict()
            temp_dict.update({'raw_review': raw_review})
            # temp_dict.update({'tagged_review': tagged_list})
            # temp_dict.update({"word_dep_review": word_dep_list})
            # print(temp_dict)

            # cleaned_words = pos_tag(full)
            # https://stackabuse.com/reading-and-writing-lists-to-a-file-in-python/
            json.dump(temp_dict, f)

            f.close()
            print("file closed")
            return temp_dict


def classify_raw(file):
    file = open(file, "r")
    for x in file:
        data = json.loads(x)

        # print(review)
        sentence_list = []
        full_review = []
        placeholder = []
        nlp = spacy.load('en_core_web_sm')
        list = data["raw_review"]
        for x in list:
            review = TextBlob(x)

            for sentence in review.sentences:
                doc = nlp(str(sentence))
                #print(sentence)
                # for each individual review in a list
                for token in doc:
                    # for each word in a list
                    # subjects include dobj
                    # adjectives include acomp and pobj

                    # subjects incl nsubj
                    # adjectives incl attr acomp
                    if token.pos_ == "NOUN" or token.pos_ == "ADJ" or token.pos_ == "ADV" or token.pos_ == "PROPN":
                        if token.dep_ == "nsubj":
                            result = (str(token))
                            # print(result)
                            if token.is_stop != "True":
                                placeholder.append(result)
                        if token.dep_ == "dobj":
                            result = (str(token))
                            # print(result)
                            if token.is_stop != "True":
                                placeholder.append(result)
                        if token.dep_ == "compound":
                            result = (str(token))
                            # print(result)
                            if token.is_stop != "True":
                                placeholder.append(result)
                        if token.dep_ == "ROOT":
                            result = (str(token))
                            # print(result)
                            if token.is_stop != "True":
                                placeholder.append(result)
                        if token.dep_ == "advmod":
                            if token.tag_ != "WRB":
                                result = (str(token))
                            # print(result)
                                if token.is_stop != "True":
                                    placeholder.append(result)
                        if token.dep_ == "amod":
                            result = (str(token))
                            # print(result)
                            if token.is_stop != "True":
                                placeholder.append(result)
                        if token.dep_ == "attr":
                            result = (str(token))
                            # print(result)
                            if token.is_stop != "True":
                                placeholder.append(result)
                        if token.dep_ == "acomp":
                            result = (str(token))
                            # print(result)
                            if token.is_stop != "True":
                                placeholder.append(result)
                        if token.dep_ == "pobj":
                            result = (str(token))
                            # print(result)
                            if token.is_stop != "True":
                                if token.text != "pm":
                                    placeholder.append(result)
                        if token.dep_ == "nsubjpass":
                            result = (str(token))
                            # print(result)
                            if token.is_stop != "True":
                                placeholder.append(result)
                        if token.dep_ == "":
                            result = (str(token))
                            # print(result)
                            if token.is_stop != "True":
                                placeholder.append(result)
                        if token.dep_ == "conj":
                            result = (str(token))
                            # print(result)
                            if token.is_stop != "True":
                                placeholder.append(result)
                        if token.dep_ == "npadvmod":
                            result = (str(token))
                            # print(result)
                            if token.is_stop != "True":
                                placeholder.append(result)
                        if token.dep_ == "cconj":
                            result = (str(token))
                            # print(result)
                            if token.is_stop != "True":

                                placeholder.append(result)

                        if token.dep_ == "neg":
                            result = (str(token))
                            # print(result)
                            if token.is_stop != "True":
                                placeholder.append(result)

                sentence_list.append(placeholder)
                placeholder = []

            full_review.append(sentence_list)
            sentence_list = []

        return full_review
