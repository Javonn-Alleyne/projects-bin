'''
randomly generate a number
give user a choice
if guessed number is correct
win
if not
lose and try again
'''

import random

print("Welcome to the Number geussing game!")
start = int(input("Please enter the starting value for you're desired range:\n"))
end = int(input("And don't forget the ending value:\n"))

while True:
    player_choice = int(input(f"Now enter a number between {start} and {end} and guess away: \n") )
    rand_num = random.randint(start, end)

    if player_choice == rand_num:
        print("WIN!")
    else:
        print("LOSE!")

    continue_choice = input("Continue?[Y/N]").lower()
    if continue_choice != 'y':
        break
    
print(f"The number generated was {rand_num}, your cohice was {player_choice}")

