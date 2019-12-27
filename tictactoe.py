#! python3

"""
tictactoe.py - is a text-based adaptation of the TicTacToe game in Python.
It features a game between an inteligent AI personality (Chip) and an human opponent.
"""

import random

print('Welcome! This is Tic Tac Toe!')
print('You will be playing against our champion AI bot, Chip!')

name = input('Okay human, what are you called?: ').capitalize()
print('\nPleased to meet you,', name)


def firstTurn():
    # Lets the human player decide the first turn.
    while True:
        first = input('Would you like to go first? (Y/N): ').upper()
        if first.startswith('Y') or first.startswith('N'):
            return first
            break
        else:
            print('\nPlease respond to the question by choosing the right option.')


def playerSymbol():
    # Lets the human player choose either X or O.
    while True:
        symbol = input(
            'Choose either X or O to represent your moves: ').upper()
        if (symbol == 'X') or (symbol == 'O'):
            return symbol
            break
        else:
            print('Incorrect symbol choice!')


board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

dummyBoard = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def printBoard(board):
    # Prints the board with the current positions.
    print('   |   |')
    print('', board[0], '|', board[1], '|', board[2])
    print('---+---+---')
    print('', board[3], '|', board[4], '|', board[5])
    print('---+---+---')
    print('', board[6], '|', board[7], '|', board[8])
    print('   |   |')


def checkFreeSquares():
    # Checks for free squares and stores their positions in a list.
    freeSquares = []
    for i in range(0, 9):
        if board[i] == ' ':
            freeSquares.append(i)
    return freeSquares


def makeMove():
    """
    Prompts human player to make a move and checks that the move is a number.
    Checks that move is available and adjusts it by substracting 1 from it
    to make it into a suitable index for the list variables we are working
    with (board, freeSquares, etc).    
    """
    while True:
        m = input('Make your move: ')
        if m.isdigit():
            myMove = int(m) - 1
        else:
            print('Invalid move!\nPlease choose a number representing a free square.')
            continue

        # checkFreeSquares()
        if myMove in checkFreeSquares():
            return myMove
            break
        else:
            print('Invalid move!\nPlease choose a number representing a free square.')


def chechForTie():
    # Checks for available squares. If non, game is tied.
    if len(checkFreeSquares()) == 0:
        return 'Tie'


def checkForWin():
    # Checks for a win using all of the winning patterns.
    if board[0] == 'X' and board[1] == 'X' and board[2] == 'X' or board[0] == 'O' and board[1] == 'O' and board[2] == 'O':
        return 'Win'
    elif board[3] == 'X' and board[4] == 'X' and board[5] == 'X' or board[3] == 'O' and board[4] == 'O' and board[5] == 'O':
        return 'Win'
    elif board[6] == 'X' and board[7] == 'X' and board[8] == 'X' or board[6] == 'O' and board[7] == 'O' and board[8] == 'O':
        return 'Win'
    elif board[0] == 'X' and board[3] == 'X' and board[6] == 'X' or board[0] == 'O' and board[3] == 'O' and board[6] == 'O':
        return 'Win'
    elif board[1] == 'X' and board[4] == 'X' and board[7] == 'X' or board[1] == 'O' and board[4] == 'O' and board[7] == 'O':
        return 'Win'
    elif board[2] == 'X' and board[5] == 'X' and board[8] == 'X' or board[2] == 'O' and board[5] == 'O' and board[8] == 'O':
        return 'Win'
    elif board[0] == 'X' and board[4] == 'X' and board[8] == 'X' or board[0] == 'O' and board[4] == 'O' and board[8] == 'O':
        return 'Win'
    elif board[2] == 'X' and board[4] == 'X' and board[6] == 'X' or board[2] == 'O' and board[4] == 'O' and board[6] == 'O':
        return 'Win'


def getStrongSquares():
    # Resets array to empty
    # Generates a list containing available strong squares for Chip's move.
    strongSquares = []
    for i in [0, 2, 6, 8]:
        if i in checkFreeSquares():
            strongSquares.append(i)
    return strongSquares


def getOtherSquares():
    """
    Resets array to empty
    Generates a list containing available squares other than strong
    squares for Chip's move.
    """
    otherSquares = []
    for i in [1, 3, 5, 7]:
        if i in checkFreeSquares():
            otherSquares.append(i)
    return otherSquares


def chipMove():
    if 4 in checkFreeSquares():
        move = 4
        return move
    elif len(getStrongSquares()) > 0:
        move = random.choice(getStrongSquares())
        return move
    elif len(getOtherSquares()) > 0:
        move = random.choice(getOtherSquares())
        return move


def playAgain():
    while True:
        q = input('Play again? (Yes or No): ').capitalize()
        if q.startswith('Y'):
            return 'Yes'
            break
        elif q.startswith('N'):
            return 'No'
            break
        else:
            print('Invalid response. Choose \'Yes\' or \'No\'.')


results = {name: 0, 'Chip': 0}


def printResult():
    print('\nGame Result')
    for k, v in results.items():
        print(' -', k + ':', v)


def resetBoard():
    global board
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    return board


if firstTurn() == 'Y':
    turn = name
else:
    turn = 'Chip'


def flipTurn():
    global turn, name
    if turn == name:
        turn = 'Chip'
    else:
        turn = name


players = {name: '', 'Chip': ''}

if playerSymbol() == 'X':
    players[name] = 'X'
    players['Chip'] = 'O'
else:
    players[name] = 'O'
    players['Chip'] = 'X'

print('\nPlayers -')
for k, v in players.items():
    print('\t', k + ':', v)


print("""\nTo make a move simply select the number representing the
position you intend to move to. This position will then be
represented by the symbol you have chosen. Below is a dummy
board showing the number positions representing each square.""")
print()
printBoard(dummyBoard)
print()
print('Let\'s Start!')
print()
printBoard(board)
print()


while True:
    print()
    print(turn + '\'s move.')

    if turn == name:
        board[makeMove()] = players[turn]
    elif turn == 'Chip':
        board[chipMove()] = players[turn]

    printBoard(board)

    if checkForWin() == 'Win':
        print(turn + ', you have WON!')
        results[turn] += 1
        printResult()

        if playAgain() == 'Yes':
            print('\nNew Game!')
            resetBoard()
            continue
        else:
            break
    elif chechForTie() == 'Tie':
        print('Gentlemen! It\'s a TIE!')
        printResult()

        if playAgain() == 'Yes':
            print('\nNew Game!')
            resetBoard()
            continue
        else:
            break
    else:
        print('\nPress \"Crtl + C\" to end the game anytime.')
        flipTurn()
