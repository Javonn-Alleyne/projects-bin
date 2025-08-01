indivi_chars = []
word_choice = input("Enter a Word: ").lower()
for x in range(len(word_choice) ):
    init = word_choice[x]
    indivi_chars.append(init)
print(indivi_chars)

player_choice = input("chose a letter: ")
if player_choice == indivi_chars[1]:
    print("yes")
else:
    print("no")