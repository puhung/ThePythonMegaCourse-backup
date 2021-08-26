import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data: #deal with country name like: Paris
        return data[w.title()]
    elif w.upper() in data:  #deal with acronyms (e.g., USA or NATO.)
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w,data.keys())[0]) #deal with similar words
        if yn == "Y":
            return data[get_close_matches(w,data.keys())[0]]
            # input the closest match as the key() in the data dictionary
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it." #deal with non existing words

# we define this variable in global scope
word = input("Enter word: ")

# then pass the variable here
output = translate(word)

#only deal with output when it is a list instead of other types like string;
if type(output) == list:
    # can not change `item` into other words.
    for item in output:        
        print(item)
else:
    print(output)