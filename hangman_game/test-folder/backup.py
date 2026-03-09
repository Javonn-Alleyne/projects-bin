import getpass #moduel to hide user input

word = []
switch = []

# word_choice = getpass.getpass(prompt = "Enter a Word: ").lower()
word_choice = input("Enter a Word: ").lower()
for x in range(len(word_choice) ):
    letter = word_choice[x]
    word.append(letter); switch.append(letter)

for y in range(len(switch)):
    switch[y] = "_"
    blanks = switch
print(f"Enjoy The Game: {blanks}")

count = 0
tries = 6
while True:
    if "_" not in blanks:
        print("You Won, the correctly guessed the word")
        break
    else:
        choice = input("enter a letter: ").lower()

        if choice in word:
            for index in range(len(word)):
                if word[index] == choice:
                    print(f"{choice}: is found @ position:{index}")
                    blanks[index] = choice
                else:
                    pass
            print(blanks)       
        else:
            tries -=1
            print(f"No letter found in word, try again. {tries} tries reamianing")
            count += 1
            if count == 6 or tries == 0:
                print(f"Game Over. The correct word was: {word_choice}")
                break