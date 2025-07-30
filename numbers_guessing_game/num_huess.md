# Project #3
number guessing game
## game logic
if player choice equals to random number generated, the the player wins, if not the player loses.

---

# code
```python
# ver1
import random

player_choice = input("Enter a number between 1 and 10\n")
rand_num = random.randint(1, 10)

if player_choice == rand_num:
	print("WIN!")
else:
	print("LOSE!")

print(rand_num)
```
## issues
logic is sound but the main issue happens with player choice. player input is entered as a string and not an integer resulting in the condition to always be false regardless of the number being equal. 
here is the random number generated is 5 and the player's choice is 5, lose will be printed despite both number being the same

```python
# ver2
import random

player_choice = int(input("Enter a number between 1 and 10\n") )
rand_num = random.randint(1, 10)

if player_choice == rand_num:
	print("WIN!")
else:
	print("LOSE!")

print(rand_num)
```

# optional adjustment
```python
# ver2.1
import random

player_choice = input("Enter a number between 1 and 10\n")
rand_num = random.randint(1, 10)

if player_choice == str(rand_num):
	print("WIN!")
else:
	print("LOSE!")

print(rand_num)
```
## convert the rand to string
instead we can also change the random number to a string to compare. since the input is inputted as a string we can change the interger random number to a string

# manually setting range values
```python
# ver3
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
```
now we let players manually set their range and and continue to play the game until they win or get tired