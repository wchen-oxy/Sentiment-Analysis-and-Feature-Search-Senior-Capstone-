import spacy
import json



print("start")
file = open(, "r")
temp = ""

for x in file:
    parsed_json = json.loads(str(x))
    raw_review = parsed_json['raw_review']
    # print(raw_review)
    filename = str("cleaned/" + file_address)

    # begin writing of text
    os.makedirs(os.path.dirname(filename), exist_ok=True)