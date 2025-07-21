# Project #2
Build a simple rock, paper scissors game

## game logic
variables: player 1, player 2
values: rock, paper, scissors

# Table logic:
| player1 value | player2 value | player1 result | player2 results |
| ------------- | ------------- | -------------- | --------------- |
| rock          | scissors      | win            | lose            |
| rock          | paper         | win            | lose            |
| paper         | scissors      | win            | lose            |
| scissors      | rock          | lose           | win             |
| paper         | rock          | lose           | win             |
| scissors      | papaer        | lose           | win             | 

# Code
```python
# ver1
print("Welcome to Rock Paper Scissors\n")

player_1 = input("Player 1. Enter your choice: Rock, Paper or Scissors:").strip().lower() # added in ver1.1
player_2 = input("Player 2. Enter your choice: Rock, Paper or Scissors:").strip().lower() # added in ver1.1

print(f"Player 1 choice:", player_1 + ' ' + "Player 2 choice:", player_2)
```
a simple set up to test input and output functions

```python
# ver1.1
print("Welcome to Rock Paper Scissors\n")

player_1 = input("Player 1. Enter your choice: Rock, Paper or Scissors:").strip().lower() # added in ver1.1
player_2 = input("Player 2. Enter your choice: Rock, Paper or Scissors:").strip().lower() # added in ver1.1

print(f"Player 1 choice:", player_1 + ' ' + "Player 2 choice:", player_2)
# player 1 logic
if player_1 == 'rock' and player_2 == 'scissors': # rock beats scissors
	print("player 1 wins")

if player_1 == 'paper' and player_2 == 'rock': # paper beats rock
	print("player 1 wins")

if player_1 == 'scissors' and player_2 == 'paper': # scissors beats paper
	print("player 1 wins")

#player 2 logic
if player_2 == 'rock' and player_1 == 'scissors':
	print("player 2 wins")

if player_2 == 'paper' and player_1 == 'rock':
	print("player 2 wins")

if player_2 == 'scissors' and player_1 == 'paper':
	print("player 2 wins")

# tie/draw logic
if player_1 == player_2:

print("Draw")
```
player logic for player 1 and player 2 and ties/draws

```python
#ver 2
print("Welcome to Rock Paper Scissors\n")

player_1 = input("Player 1. Enter your choice: Rock, Paper or Scissors:").strip().lower() # added in ver1.1
player_2 = input("Player 2. Enter your choice: Rock, Paper or Scissors:").strip().lower() # added in ver1.1

print(f"Player 1 choice:", player_1 + ' ' + "Player 2 choice:", player_2)

while True:
	# player 1 logic
	if player_1 == 'rock' and player_2 == 'scissors': # rock beats scissors
		print("player 1 wins")
	
	if player_1 == 'paper' and player_2 == 'rock': # paper beats rock
		print("player 1 wins")
	
	if player_1 == 'scissors' and player_2 == 'paper': # scissors beats paper
		print("player 1 wins")
	
	# player 2 logic
	if player_2 == 'rock' and player_1 == 'scissors':
		print("player 2 wins")
	
	if player_2 == 'paper' and player_1 == 'rock':
		print("player 2 wins")
	
	if player_2 == 'scissors' and player_1 == 'paper':
		print("player 2 wins")
	
	# tie/draw logic
	if player_1 == player_2:
		print("Draw")
	
	referee = input("Continue: [Y/N]").lower()
	if referee != 'y':
		break:

print("Game End")
```
keep the game going until the players quit
error: was returning the last result in stead of the player input prompts

```python
#ver 3
while True:
	print("Welcome to Rock Paper Scissors\n")
	player_1 = input("Player 1. Enter your choice: Rock, Paper or Scissors:").strip().lower() # added in ver1.1
	player_2 = input("Player 2. Enter your choice: Rock, Paper or Scissors:").strip().lower() # added in ver1.1
	print(f"Player 1 choice:", player_1 + ' ' + "Player 2 choice:", player_2)
	
	# player 1 logic
	if player_1 == 'rock' and player_2 == 'scissors': # rock beats scissors
		print("player 1 wins")
	
	if player_1 == 'paper' and player_2 == 'rock': # paper beats rock
		print("player 1 wins")
	
	if player_1 == 'scissors' and player_2 == 'paper': # scissors beats paper
		print("player 1 wins")
	
	#plyaer 2 logic
	if player_2 == 'rock' and player_1 == 'scissors':
		print("player 2 wins")
	
	if player_2 == 'paper' and player_1 == 'rock':
		print("player 2 wins")
	
	if player_2 == 'scissors' and player_1 == 'paper':
		print("player 2 wins") 
	
	# tie/draw logic
	if player_1 == player_2:
		print("Draw")
	
	referee = input("Continue: [Y/N]").lower()
	if referee != 'y':
		break

print("Game End")
```
move while statement at the top to start the player input prompts again

```python
# ver 3.1
def referee():
	referee_choice = input("Continue: [Y/N]").lower()
	if referee_choice != 'y':
		return referee
		
while True:
	print("Welcome to Rock Paper Scissors\n")
	player_1 = input("Player 1. Enter your choice: Rock, Paper or Scissors:").strip().lower() # added in ver1.1
	player_2 = input("Player 2. Enter your choice: Rock, Paper or Scissors:").strip().lower() # added in ver1.1
	print(f"Player 1 choice:", player_1 + ' ' + "Player 2 choice:", player_2)
	
	# player 1 logic
	if player_1 == 'rock' and player_2 == 'scissors': # rock beats scissors
		print("player 1 wins")
	
	if player_1 == 'paper' and player_2 == 'rock': # paper beats rock
		print("player 1 wins")
	
	if player_1 == 'scissors' and player_2 == 'paper': # scissors beats paper
		print("player 1 wins")
	
	#plyaer 2 logic
	if player_2 == 'rock' and player_1 == 'scissors':
		print("player 2 wins")
	
	if player_2 == 'paper' and player_1 == 'rock':
		print("player 2 wins")
	
	if player_2 == 'scissors' and player_1 == 'paper':
		print("player 2 wins") 
	
	# tie/draw logic
	if player_1 == player_2:
		print("Draw")
	
	referee()
	break

print("Game End")

```
make player choice to continue a function because reason and efficiency i think)
error: game breaks after first run regardless of choice.

# ai help
completely restructure project. too lazy to fix, so reverted to ver 3

# back on my own
```python
# ver3.2
player_1_list=[]
player_2_list=[]

while True:
	print("Welcome to Rock Paper Scissors\n")
	player_1 = player_1_list.append( input("Player 1. Enter your choice: Rock, Paper or Scissors:").strip().lower() )# added in ver1.1
	player_2 = player_2_list.append( input("Player 2. Enter your choice: Rock, Paper or Scissors:").strip().lower() )# added in ver1.1
	# print(f"Player 1 choice:", player_1 + ' ' + "Player 2 choice:", player_2)
	# player_1_list.append(input)
	
	# player 1 logic
	if player_1 == 'rock' and player_2 == 'scissors': # rock beats scissors
		print("player 1 wins")
	
	if player_1 == 'paper' and player_2 == 'rock': # paper beats rock
		print("player 1 wins")
	
	if player_1 == 'scissors' and player_2 == 'paper': # scissors beats paper
		print("player 1 wins")
	
	#plyaer 2 logic
	if player_2 == 'rock' and player_1 == 'scissors':
		print("player 2 wins")
	
	if player_2 == 'paper' and player_1 == 'rock':
		print("player 2 wins")
	
	if player_2 == 'scissors' and player_1 == 'paper':
		print("player 2 wins")
	
	# tie/draw logic
	if player_1 == player_2:
		print("Draw")
	
	referee_choice = input("Continue: [Y/N]").lower()
		if referee_choice != 'y':
			break

print("Game End")
print(player_1_list)
print(player_2_list)
```
return player choices in a list after game is over

```python
# ver 3.2.1
player_1_choice=[]
player_2_chioce=[]

while True:
	print("Welcome to Rock Paper Scissors\n")
	player_1 = player_1_choice.append( input("Player 1. Enter your choice: Rock, Paper or Scissors:").strip().lower() )# added in ver1.1
	player_2 = player_2_chioce.append( input("Player 2. Enter your choice: Rock, Paper or Scissors:").strip().lower() )# added in ver1.1
	
	# player 1 logic
	if player_1 == 'rock' and player_2 == 'scissors': # rock beats scissors
		print("player 1 wins")
	
	if player_1 == 'paper' and player_2 == 'rock': # paper beats rock
		print("player 1 wins")
	
	if player_1 == 'scissors' and player_2 == 'paper': # scissors beats paper
		print("player 1 wins")
	
	#plyaer 2 logic
	if player_2 == 'rock' and player_1 == 'scissors':
		print("player 2 wins")
	
	if player_2 == 'paper' and player_1 == 'rock':
		print("player 2 wins")
	
	if player_2 == 'scissors' and player_1 == 'paper':
		print("player 2 wins")
		
	# tie/draw logic
	if player_1 == player_2:
		print("Draw")
	
	referee_choice = input("Continue: [Y/N]").lower()
		if referee_choice != 'y':
			break

print("Game End")
print(player_1_choice)
print(player_2_chioce)
player_1_length = len(player_1_choice)
player_2_length = len(player_2_chioce)
print(player_1_length)
print(player_2_length)
```

```python
# ver 3.2.2
player_1_choice=[]
player_2_chioce=[]

while True:
	print("Welcome to Rock Paper Scissors\n")
	player_1 = player_1_choice.append( input("Player 1. Enter your choice: Rock, Paper or Scissors:").strip().lower() )# added in ver1.1
	player_2 = player_2_chioce.append( input("Player 2. Enter your choice: Rock, Paper or Scissors:").strip().lower() )# added in ver1.1
	
	# player 1 logic
	if player_1 == 'rock' and player_2 == 'scissors': # rock beats scissors
		print("player 1 wins")
	
	if player_1 == 'paper' and player_2 == 'rock': # paper beats rock
		print("player 1 wins")
	
	if player_1 == 'scissors' and player_2 == 'paper': # scissors beats paper
		print("player 1 wins")
	
	#plyaer 2 logic
	if player_2 == 'rock' and player_1 == 'scissors':
		print("player 2 wins")
	
	if player_2 == 'paper' and player_1 == 'rock':
		print("player 2 wins")
	
	if player_2 == 'scissors' and player_1 == 'paper':
		print("player 2 wins")
		
	# tie/draw logic
	if player_1 == player_2:
		print("Draw")
	
	referee_choice = input("Continue: [Y/N]").lower()
		if referee_choice != 'y':
			break

print("Game End")
print(player_1_choice)
print(player_2_chioce)
```
length is not important as it will be the same

```python
# ver 3.2.3
player_1_choice=[]
player_2_choice=[]

while True:
	print("Welcome to Rock Paper Scissors\n")
	player_1 = input("Player 1. Enter your choice: Rock, Paper or Scissors:").strip().lower() # added in ver1.1
	player_2 = input("Player 2. Enter your choice: Rock, Paper or Scissors:").strip().lower() # added in ver1.1

	player_1_choice.append(player_1)
	player_2_choice.append(player_2)
	
	# player 1 logic
	if player_1 == 'rock' and player_2 == 'scissors': # rock beats scissors
		print("player 1 wins")
	
	if player_1 == 'paper' and player_2 == 'rock': # paper beats rock
		print("player 1 wins")
	
	if player_1 == 'scissors' and player_2 == 'paper': # scissors beats paper
		print("player 1 wins")
	
	#plyaer 2 logic
	if player_2 == 'rock' and player_1 == 'scissors':
		print("player 2 wins")
	
	if player_2 == 'paper' and player_1 == 'rock':
		print("player 2 wins")
	
	if player_2 == 'scissors' and player_1 == 'paper':
		print("player 2 wins")
		
	# tie/draw logic
	if player_1 == player_2:
		print("Draw")
	
	referee_choice = input("Continue: [Y/N]").lower()
		if referee_choice != 'y':
			break

print("Game End")
print(player_1_choice)
print(player_2_choice)
```
game was printig darw after each players choice. that is no beuno. fixed my appending properly