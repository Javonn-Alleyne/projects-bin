import ast
import random

word_list = []

def random_word():
    with open('word_list.txt','r') as file:
        content = file.readlines()
        for line in content:
            words = ast.literal_eval(line)
            word_list.append(words)

    rand = random.choice(word_list)
    return rand['word'], rand['hint']

# def random_hint():
#     with open('word_list.txt','r') as file:
#         word_list = [ast.literal_eval(line) for line in file.readlines()]

#         rand = random.choice(word_list)
#         return rand['hint']
# select = rand.get("id")
# print(select)
# print(f"word: {rand.get('word')}")
# print(f"hint: {rand.get('hint')}")