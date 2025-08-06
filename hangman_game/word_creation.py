'''
Adding new words
here the player can add as many words as they please
the script chceks for all the lines in the file first to retreieve the last id
the "words" as stored as dictioanraires, they ecah have:
    an 'id' for quick easy references
    a 'hint' cant guess if you dont know what you randomly get
'''

hangman_word_list = [] #list for words and new words

def next_id(): #player does not know the ids for the words, so we chcek it and automatically update it with each entry
    try:
        with open("word_list.txt",'r') as file: #open file in read only mode to prevetn new entries
            return len(file.readlines() ) + 1 #chcek for all lines in the file
    except FileNotFoundError: #only trigger if file not found
        return 1
current_id = next_id() #get the last id of the file list

while True: #loop to continuously add more words and hints to the word list
    word = input("Enter a word: \n")
    hint = input("Give it a hint: ")

    hangman_word_list.append( #dictionrary to store the players input
        {
            "id": current_id,
            "word": word,
            "hint": hint,
        }
    )

    current_id += 1 #update the id for the new entry

    contin = input("Do you want to enter another word?[Y/N]").lower() #continue entering words as long as 'y' is chosen, else stop adding new words
    if contin != 'y':
        break

with open("word_list.txt",'a') as file: #poen the file and add the new content to it
    for item in hangman_word_list:
        file.write(f"{item}\n")
print(f"Saved word in:{hangman_word_list}") #message to tell the player their updates are valid