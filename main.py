# This is a rock paper scissors game.
# The player will be playing against the computer.
# Provides statistics when the player quits the game.

import message
import random
import traceback
import rock_paper_scissors

def main():
    try:
        gameCount = 0 # initializes the game counter
        play = [] # initializes the array
        while True:
            message.menu() # prints the menu
            playerChoice = choice(input("Menu Option: ")) # calls the choice function
            computerChoice = computer() # calls the computer function
            print('\n**************************')
            print(f'Game: {gameCount}')
            print(f'Computer: {computerChoice}')
            print(f'Player: {playerChoice}')
            if playerChoice == 'Rock' or playerChoice == 'Paper' or playerChoice == 'Scissor':
                gameCount += 1
                print('\n**********Result**********')
                gameWinner = (game(playerChoice, computerChoice))
                play.append(gameWinner) # The game winner is added to the array for each game
                print('**************************')
            elif playerChoice == 'Quit':
                message.end()
                comp, player, tie = satistics(play) # calls the statistics function
                print('**********Statistics**********\n'
                f'Player Wins: {player} times\n' # prints the player stats
                f'Computer Wins: {comp} times\n' # prints the computer stats
                f'Ties: {tie} times') # prints the number of ties
                print('******************************')
                break
            else:
                print('\n**********Try Again*************\n')
                print(playerChoice) # prints when the callers choice is not in the option
                print('\n********************************')
                
    except Exception:
        traceback.print_exc()

# Generates the computer choice by picking randomly from the value in the array
def computer():
    rockPaperScissors = ['Rock', 'Paper', 'Scissor']
    return random.choice(rockPaperScissors)

# Returns the choice depending on the player choice
def choice(menuOption):
    if menuOption == '1':
        return 'Rock'
    elif menuOption == '2':
        return 'Paper'
    elif menuOption == '3':
        return 'Scissor'
    elif menuOption == '4':
        return 'Quit'
    else:
        return 'Your choice is not in the menu' # Returns this value if the choice is not in the menu

# Determines who wins and losses on each game
def game(player, computer):
    if player == 'Rock' and computer == 'Scissor':
        message.playerWins() # prints the player wins
        message.rock() # prints the rock message
        return rock_paper_scissors.Game(player, computer, 'Player').winner
    elif player == 'Paper' and computer == 'Rock':
        message.playerWins()
        message.paper() # prints the paper message
        return rock_paper_scissors.Game(player, computer, 'Player').winner
    elif player == 'Scissor' and computer == 'Paper':
        message.playerWins()
        message.scissor() # prints the scissor message
        return rock_paper_scissors.Game(player, computer, 'Player').winner
    elif computer == 'Rock' and player == 'Scissor':
        message.computerWins() # prints the computer wins
        message.rock()
        return rock_paper_scissors.Game(player, computer, 'Computer').winner
    elif computer == 'Paper'and player == 'Rock':
        message.computerWins()
        message.paper()       
        return rock_paper_scissors.Game(player, computer, 'Computer').winner
    elif computer == 'Scissor' and player == 'Paper':
        message.computerWins()
        message.scissor()
        return rock_paper_scissors.Game(player, computer, 'Computer').winner
    else:
        message.tie() # prints the tie message

# Counts the how many times each player wins and ties the game
def satistics(gameWinner):
    comp = 0
    player = 0
    tie = 0

    for winner in gameWinner:
        if winner == 'Computer':
            comp += 1 # Counts how many times the computer wins
        elif winner == 'Player':
            player += 1 # Counts how many times the player wins
        else:
            tie += 1 # counts the number of game tie
    return comp, player, tie


if __name__=='__main__':
    main()