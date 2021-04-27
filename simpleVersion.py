import json
import difflib   # python library to compare text
from difflib import SequenceMatcher
from difflib import get_close_matches
SequenceMatcher(None, )  # None ia s argument by default called isjunk

data = json.load(open('data.json'))



def translate(w):
    w = w.lower()   # because in data.json
    if w in data:
        return data[w]

    elif w.title() in data:
        return data[w.title()]

    elif w.upper() in data:
        return data[w.upper()]

    elif len(get_close_matches(w, data.keys())) > 0:
         yn = input('Did you mean %s instead? Enter Y if Yes, enter N if No: ' % get_close_matches(w, data.keys())[0])
         if yn == 'Y' :
             return data[get_close_matches(w, data.keys())[0]]
         elif yn == 'N':
             return 'The word does not exist, please double check the spelling. '
         else:
             return 'Please enter Y or N, thanks. '


    else:
        return 'The word does not exist, please check again..... '


word = input('Please enter a word: ')

output = translate(word)     # user friendly

if type(output) ==  list:
    for item in output:
        print(item)
    else:
        print(output)

