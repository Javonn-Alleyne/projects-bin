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
print("List of Player 1's choices:", player_1_choice)
print("List of Player 2's choices:", player_2_choice)