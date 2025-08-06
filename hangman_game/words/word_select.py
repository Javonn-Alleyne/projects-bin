import ast
import random

word_choice = []

with open('word_list.txt','r') as file:
    content = file.readlines()
    for line in content:
        words = ast.literal_eval(line)
        word_choice.append(words)

rand = random.choice(word_choice)
select = rand.get("id")
print(select)
print(f"word: {rand.get('word')}")
print(f"hint: {rand.get('hint')}")
