import math
import random
from random import *
import pprint

board={'tL':'', 'tM':'', 'tR':'',
       'mL':'', 'mM':'', 'mR':'',
       'lL':'', 'lM':'', 'lR':''}

def tic(theBoard):
    print(theBoard['tL'] + '|' + theBoard['tM'] + '|' + theBoard['tR'])
    print('-+-+-')
    print(theBoard['mL'] + '|' + theBoard['mM'] + '|' + theBoard['mR'])
    print('-+-+-')
    print(theBoard['lL'] + '|' + theBoard['lM'] + '|' + theBoard['lR'])
turn = 'X'

for i in range(9):
    tic(board)
    print('Turn for ' +turn+ '. Move on which space?')
    print('Please notice that the indices are specifies from top left to top right as: tL, tM, tR. This is true for rest of rows too.')
    move=input()
    board[move]=turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    tic(board)

    
