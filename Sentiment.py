from textblob import TextBlob
import json

text = '''
The titular threat of The Blob has always struck me as the ultimate movie
monster: an insatiably hungry, amoeba-like mass able to penetrate
virtually any safeguard, capable of--as a doomed doctor chillingly
describes it--"assimilating flesh on contact.
Snide comparisons to gelatin be damned, it's a concept with the most
devastating of potential consequences, not unlike the grey goo scenario
proposed by technological theorists fearful of
artificial intelligence run rampant.
'''
file = open("cleaned/output/cleaned.txt", "r")
for x in file:
    print(x)


#     blob = TextBlob(text)
# for sentence in blob.sentences:
#     print(sentence.sentiment)
