# This is a rock paper scissors game
# The player will be playing against the computer

import message
import random
import traceback
import rock_paper_scissors

def main():
    try:
        gameWinner = []
        while True:
           message.menu()
           playerChoice = choice(input("Menu Option: "))
           computerChoice = computer()
           print(f'Computer: {computerChoice}')
           if playerChoice == 'Rock' or playerChoice == 'Paper' or playerChoice == 'Scissor':
               print('\n**********Result**********')
               result = (game(playerChoice, computerChoice))
               gameWinner.append(result)
               print('**************************')
           elif playerChoice == 'Quit':
               message.end()
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
               print('**********Statistics**********\n'
                f'Player Wins: {player} times\n'
                f'Computer Wins: {comp} times\n'
                f'Ties: {tie} times')
               print('******************************')
               break
           else:
               print('\n**********Try Again*************\n')
               print(playerChoice)
               print('\n********************************')
               
    except Exception:
        traceback.print_exc()
        # print('something went wrong')

def computer():
    rockPaperScissors = ['Rock', 'Paper', 'Scissor']
    return random.choice(rockPaperScissors)

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
        return 'Your choice is not in the menu'
        
def game(player, computer):
    if player == 'Rock' and computer == 'Scissor':
        message.playerWins()
        message.rock()
        return rock_paper_scissors.RockPaperScissor(player, computer, 'Player').winner
    elif player == 'Paper' and computer == 'Rock':
        message.playerWins()
        message.paper()
        return rock_paper_scissors.RockPaperScissor(player, computer, 'Player').winner
    elif player == 'Scissor' and computer == 'Paper':
        message.playerWins()
        message.paper()
        return rock_paper_scissors.RockPaperScissor(player, computer, 'Player').winner
    elif computer == 'Rock' and player == 'Scissor':
        message.computerWins()
        message.rock()
        return rock_paper_scissors.RockPaperScissor(player, computer, 'Computer').winner
    elif computer == 'Paper'and player == 'Rock':
        message.computerWins()
        message.paper()       
        return rock_paper_scissors.RockPaperScissor(player, computer, 'Computer').winner
    elif computer == 'Scissor' and player == 'Paper':
        message.computerWins()
        message.paper()
        return rock_paper_scissors.RockPaperScissor(player, computer, 'Computer').winner
    else:
        message.tie()
        

if __name__=='__main__':
    main()