# theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
# 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
# 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
# def printBoard(board):
#  print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
#  print('-+-+-')
#  print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
#  print('-+-+-')
#  print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
# printBoard(theBoard)

#---------------------2---------------------------------------

theBoard = {'top-L': 'O', 'top-M': 'O', 'top-R': 'O', 'mid-L': 'X', 'mid-M':
'X', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': 'X'}
def printBoard(board):
 print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
 print('-+-+-')
 print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
 print('-+-+-')
 print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
printBoard(theBoard)

