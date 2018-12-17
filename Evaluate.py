import spacy
import csv
import spacy
import nltk

nlp = spacy.load('en_core_web_sm')
file = 'Evaluation/POS/positive.csv'

count = 0
array1 = []
array2 = []
with open(file, newline='') as csvfile:
    spamreader1 = csv.reader(csvfile, delimiter=' ', quotechar='|')
    correct = 0
    total = 0
    temp1 = ""
    temp2 = ""

    # print(spamreader2)
    for row in spamreader1:
        for x in row:

            y = x.replace(",", " ")
            doc = nlp(y)
            for token in doc:
                # print(token.pos_)
                array1.append(token.pos_)


count = 0
correct = 0
with open('Evaluation/POS/split_correct.csv', newline='') as csvfile:
    spamreader1 = csv.reader(csvfile, delimiter=' ', quotechar='|')
    correct = 0
    total = 0
    temp1 = ""
    temp2 = ""

    # print(spamreader2)
    for row in spamreader1:
        for x in row:
            if x == array1[count]:
                correct += 1
        count += 1
print("This is the number of correct: " + str(correct) + "out of " + str(count))
percent = correct/count
print(percent)
