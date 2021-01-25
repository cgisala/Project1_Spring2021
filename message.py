"""This file will house all of the messages that will be printed in the program"""

def menu():
    print('\nMenu: \n'
    '1: Rock\n'
    '2: Paper\n'
    '3: Scissor\n'
    '4: Quit game\n')

def paper():
    print('Paper covers rock')

def rock():
    print('Rock crushes scissors')

def scissor():
    print('Scissors cut paper')

def tie():
    print('Tie')

def end():
    print('\nThank you for playing the game\n')

def playerWins():
    print('Player Wins.')

def computerWins():
    print('Computer Wins!')