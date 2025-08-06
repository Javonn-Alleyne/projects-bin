'''
Hangman gGame
player gets a random word and has to guess it in six tries else they fail
'''

import word_select # load in the word select file to randomly chose a word for a list of words

def hangman_game():
    select, hint = word_select.random_word() #get the word and its hint from the word_select.py file
    print(f"Hint: {hint}") #give the player a hint to guess what the word is

    selected_word = [] # list for holding the individual letters of the word
    switch_to_blanks = [] # list for holding the individual lerters of the word that will be converted to blanks, ("_")

    for x in range(len(select) ): #loop throguh each letter of the word and add them as individual chars. (break the string into individual chars)
        letter = select[x]
        selected_word.append(letter)
        switch_to_blanks.append(letter) #add to switch_to_blanks list to avoid overwriting the selected_word list

    for y in range(len(switch_to_blanks)): #take those chars and replace them with blanks, ("_")
        switch_to_blanks[y] = "_"
        word_blanks = switch_to_blanks
    print("Welcome to Hangman, Enjoy The Game")

    count = 0 #count as a back up if tries fails, because reasons ;)
    tries = 6
    while True:
        if "_" not in word_blanks: #if no more blanks end the game
            print(f"You Won, the correctly guessed the word, {select}")
            break
        else: #play game as normal
            choice = input("Enter a letter: ").lower()

            if choice in selected_word: #if letter exist, replace the blank at its position which is refernced in the word list
                for index in range(len(selected_word)):
                    if selected_word[index] == choice:
                        print(f"{choice}: is found @ position:{index}")
                        word_blanks[index] = choice
                    else:
                        pass
                print(word_blanks)       
            else: 
                tries -=1 #if incorrect leeter gues, add a body part
                print(f"That letter is not found in the word. Try again. {tries} tries reamianing")
                count += 1
                if count == 6 or tries == 0: #if player cant get the word in 6 tries, end game
                    print(f"Game Over. You ran out of tries. The correct word was: {select}")
                    break

if __name__ == "__main__": #dont create a blackhole
    hangman_game()