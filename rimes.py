# This scrip allows to find words that rime with a word that the user inputs using the datamuse API.

import requests
import json

def findRimes(string):

    kval_pairs = {'rel_rhy': user_word}                                         # spefify parameters
    page = requests.get("https://api.datamuse.com/words", params=kval_pairs)    # construct the URL 
    content = page.json()   # transform the JSON response into a python object

    for inside in content:
        print('A word that rimes with' + user_word + ' is:' , inside['word'])


user_word = input('I need words that rime with: ')
print('---------- Working on it ----------')

findRimes(user_word)

print('Done!')