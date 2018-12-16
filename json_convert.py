# Begin Section of Code Specifically Designed for the Json File
import json


def load_dict(input_data):
    all_dict = dict()
    #create a reference file for the inputted review data
    file = open(input_data, "r")
    #initialize the input to blank
    input = ""
    #check if the input file is a test one or the real one
    if input_data == "yelp_dataset/yelp_academic_dataset_review.json" or input_data == "yelp_dataset/testfile.json":
        input = "text"
    else:
        input = 'caption'

    #     parsed_json = json.loads(str(file))
    #begin parsing throug the json file
    for x in file:
        # load each set containing review information
        parsed_json = json.loads(str(x))
        name_entry = parsed_json['business_id']
        #print(name_entry)
        # check if the business name does not exist yet
        #print(name_entry)
        if name_entry in all_dict:
            #print("yes")
            #check if the new review text is empty
            if parsed_json[input] == '':
                continue
            #print(parsed_json[input])
            #create a temporary list corresponding to the value assoc. with key
            templist = all_dict[name_entry]
            #append the new review data into that temporary list
            templist.append(parsed_json[input])
            #update value to key in the dictionary
            all_dict.update({name_entry:templist})



        else:
            # if false, create a new dictionary but first create a container list
            list = [parsed_json[input]]
            if list == ['']:
                continue
            #print("here")
            #print(list)
            all_dict.update({name_entry:list})
            # add dictionary to superset dictionary
    return all_dict

    # print("done")
    # print(all_dict['3Nw_mnpdpqtAJ5bRt0jsvw'])


# file = "yelp_dataset/yelp_academic_dataset_review.json"
# cleaned_file = Sort(file)
