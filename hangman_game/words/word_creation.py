hangman_word_list = []

def next_id():
    try:
        with open("word_list.txt",'r') as file:
            return len(file.readlines() ) + 1
    except FileNotFoundError:
        return 1
current_id = next_id()

while True:
    word = input("Enter a word: \n")
    hint = input("Give it a hint: ")

    hangman_word_list.append(
        {
            "id": current_id,
            "word": word,
            "hint": hint,
        }
    )

    current_id += 1

    contin = input("Do you want to enter another word?").lower()
    if contin != 'y':
        break

with open("word_list.txt",'a') as file:
    for item in hangman_word_list:
        file.write(f"{item}\n")
print(f"Saved word in:{hangman_word_list}")