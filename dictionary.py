import json
from difflib import get_close_matches

dic_data = json.load(open("data.json"))

def show_Output(word):
    if word in dic_data:
        return dic_data[word]
    elif word.title() in dic_data:
        return dic_data[word.title()]
    elif word.upper() in dic_data:
        return dic_data[word.upper()]
    elif len(get_close_matches(word, dic_data.keys())) > 0 :
        print("Did you mean %s ? Enter Yes or No" % get_close_matches(word, dic_data.keys())[0])
        choice = input()
        choice = char(choice.lower())
        if choice is 'y' :
            new_word = get_close_matches(word, dic_data.keys())[0]
            return dic_data[new_word]
        elif choice is 'n':
            print("The word doesn't exit. Please check for any mistake")
    else:
        print("The word doesn't exit. Please check for any mistake")

word = input("Enter a word : ")
word = word.lower()
final_output = show_Output(word)

type_check = type(final_output)

if type_check is list:
    for f in final_output:
        print(f)
else:
    print(final_output)
    
