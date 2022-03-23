# This scrip allows to find words that rime with a word that the user inputs using the datamuse API.

import requests
import json

def findRimes(string):

    kval_pairs = {'rel_rhy': string}                                            # spefify parameters
    page = requests.get("https://api.datamuse.com/words", params=kval_pairs)    # construct the URL 
    content = page.json()                                                       # transform the JSON response into a python object

    words = []                 
    for inside in content:
        words.append(inside['word'])                                            # add each word to the empty list
        print('A word that rimes with' + user_word + ' is:' , inside['word'])   # print the words on the screen in a nice format
    return words                                                                # return a list of the words that can be used in other parts of the program

user_word = input('I need words that rime with: ')
print('---------- Working on it ----------')

findRimes(user_word)

print('Done!')
