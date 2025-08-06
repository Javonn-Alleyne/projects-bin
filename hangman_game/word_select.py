'''
Random word choice
you have no friends and want to play hangman
no fun if you always get the word right
    *becuase you put it in to start the game*
so instead you make sure each round is a randomly chosen word from a list
'''

import ast
import random

word_list = [] #list to hold multiple dictionaries

def random_word(): #function so it can be imported and used by the hangman_main.py file
    with open('word_list.txt','r') as file: #open file in read mode, cannnot add any new items
        content = file.readlines()
        for line in content: #loop through the file and add each dictionary to the list
            words = ast.literal_eval(line) #converts the dictionray to a string, else error.
            word_list.append(words) #add the dictionary to the list

    rand = random.choice(word_list) #randomly select a word with its hint
    return rand['word'], rand['hint'] #allows the word and hint to be fresenced by the main py file

# #Mics.
# def random_hint():
#     with open('word_list.txt','r') as file:
#         word_list = [ast.literal_eval(line) for line in file.readlines()]

#         rand = random.choice(word_list)
#         return rand['hint']
# select = rand.get("id")
# print(select)
# print(f"word: {rand.get('word')}")
# print(f"hint: {rand.get('hint')}")