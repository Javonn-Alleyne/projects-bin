import word_select

def main():
    select, hint = word_select.random_word()
    print(f"Hint: {hint}")

    word = []
    switch = []

    for x in range(len(select) ):
        letter = select[x]
        word.append(letter)
        switch.append(letter)

    for y in range(len(switch)):
        switch[y] = "_"
        blanks = switch
    print("Welcome to Hangman, Enjoy The Game")

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
                    print(f"Game Over. The correct word was: {select}")
                    break

if __name__ == "__main__":
    main()