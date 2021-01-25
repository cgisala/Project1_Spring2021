# This is a rock paper scissors game
# The player will be playing against the computer

import message
import random
import traceback
import rock_paper_scissors

def main():
    try:
        gameWinner = [] # initializes the array
        while True:
           message.menu() # prints the menu
           playerChoice = choice(input("Menu Option: ")) # calls the choice function
           computerChoice = computer() # calls the computer function
           print(f'Computer: {computerChoice}')
           if playerChoice == 'Rock' or playerChoice == 'Paper' or playerChoice == 'Scissor':
               print('\n**********Result**********')
               result = (game(playerChoice, computerChoice))
               gameWinner.append(result) # The game winner is added to the array for each geame
               print('**************************')
           elif playerChoice == 'Quit':
               message.end()
               comp, player, tie = satistics(gameWinner) # calls the statistics function
               print('**********Statistics**********\n'
                f'Player Wins: {player} times\n' # prints the player stats
                f'Computer Wins: {comp} times\n' # prints the computer stats
                f'Ties: {tie} times') # prints the number of ties
               print('******************************')
               break
           else:
               print('\n**********Try Again*************\n')
               print(playerChoice)
               print('\n********************************')
               
    except Exception:
        traceback.print_exc()
        # print('something went wrong')

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
        return 'Your choice is not in the menu' # Retruens this value if the choice is not in the menu

# Determines who wins and losses on each game
def game(player, computer):
    if player == 'Rock' and computer == 'Scissor':
        message.playerWins() # prints the player wins
        message.rock() # prints the rock message
        return rock_paper_scissors.RockPaperScissor(player, computer, 'Player').winner
    elif player == 'Paper' and computer == 'Rock':
        message.playerWins()
        message.paper() # prints the paper message
        return rock_paper_scissors.RockPaperScissor(player, computer, 'Player').winner
    elif player == 'Scissor' and computer == 'Paper':
        message.playerWins()
        message.scissor() # prints the scissor message
        return rock_paper_scissors.RockPaperScissor(player, computer, 'Player').winner
    elif computer == 'Rock' and player == 'Scissor':
        message.computerWins() # prints the computer wins
        message.rock()
        return rock_paper_scissors.RockPaperScissor(player, computer, 'Computer').winner
    elif computer == 'Paper'and player == 'Rock':
        message.computerWins()
        message.paper()       
        return rock_paper_scissors.RockPaperScissor(player, computer, 'Computer').winner
    elif computer == 'Scissor' and player == 'Paper':
        message.computerWins()
        message.scissor()
        return rock_paper_scissors.RockPaperScissor(player, computer, 'Computer').winner
    else:
        message.tie() # prints the tie message

# Counts the how many times each player wins and ties the game
def satistics(gameWinner):
    count = 0
    comp = 0
    player = 0
    tie = 0
    for winner in gameWinner:
        count += 1
        if winner == 'Computer':
            comp += 1
        elif winner == 'Player':
            player += 1
        else:
            tie += 1
    return comp, player, tie


if __name__=='__main__':
    main()