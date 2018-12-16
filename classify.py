import spacy

nlp = spacy.load('en_core_web_sm')


def pos_tag(review):
    #print(review)
    full_review = []
    doc = nlp(review)
    #for each individual review in a list
    for token in doc:
        #for each word in a list
        if token.pos_ == "PROPN":
            result = ("Proper Noun is " + str(token))
            #print(result)
            full_review.append(result)
        if token.pos_ == "NOUN":
            result = ("Noun is " + str(token))
            #print(result)
            full_review.append(result)
        if token.pos_ == "ADJ":
            result = ("ADJ is " + str(token))
            #print(result)
            full_review.append(result)
    return full_review



def word_dep(review):
    #print(review)
    full_review = []
    placeholder = []
    doc = nlp(review)
    #for each individual review in a list
    for token in doc:
        #for each word in a list
        if token.dep_ == "nsubj":
            result = ("nsubj is " + str(token))
            #print(result)
            placeholder.append(result)
        if token.dep_ == "amod":
            result = ("amod is " + str(token))
            #print(result)
            placeholder.append(result)
        if token.dep_ == "pobj":
            result = ("pobj is " + str(token))
            #print(result)
            placeholder.append(result)
        if str(token) == ".":
            full_review.append(placeholder)
            placeholder = []

    print(full_review)

    return full_review



