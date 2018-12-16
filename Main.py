from json_convert import load_dict
from json_to_main import sort
from classify_v2 import file_create, classify
import json

file1 = "yelp_dataset/yelp_academic_dataset_review.json"
file2 = 'yelp_dataset/yelp_academic_dataset_photo.json'
file3 = 'yelp_dataset/testfile.json'
file4 = 'raw_output/f5O7v_X_jCg2itqacRfxhg.txt'

# def section_one():
#     #This section of Code Converts things
#     #Use json_convert's sort to clean the data
#     print("start")
#     cleaned_dict = load_dict(file1)
#     print(cleaned_dict)
#     print("middle")
#     #begin cleaning data
#     #use json_to_main to sort data into positive and negative
#     #sort(cleaned_dict)
#     print("finished")
def section_two(address):
    #This section of code will be our next classifier:

    dependencies = classify(address)
    return dependencies
#section_one()
#create the list of relevant things
#file_create(file4)
#sort out the stuff
address = "cleaned/" + file4
list = section_two(address)
with open("cleaned/output/cleaned.txt", "a+") as finished:
    json.dump(list, finished)


