from time import sleep
import curses

board = []
with open('sudoku.txt','r') as file:
    for line in file:
         board.append(list(map(int,line.strip())))

def valid(row, col, value):
  for c in range(9):
    if board[row][c] == value and c != col:
      return False # Duplicate Row Item
  for r in range(9):
    if board[r][col] == value and r != row:
      return False # Duplicate Column Item
  block = ((row//3)*3, (col//3)*3)
  for i in range(block[0], block[0]+3):
    for j in range(block[1], block[1]+3):
      if(board[i][j] == value and (i,j) != (row, col)):
        return False # Duplicate Block Item
  return True

def fill(cell):
  printBoard()
  if(cell == 81):
    return True
  row = cell//9
  col = cell%9
  if(board[row][col] != 0):
    return fill(cell+1)
  else:
    for i in range(1,10):
      if(valid(row, col, i)):
        board[row][col] = i
        if(fill(cell+1)):
          return True
        board[row][col] = 0
    return False

def printBoard():
  screen.clear()
  word = ""
  for i, row in enumerate(board):
    if i % 3 == 0:
        word += str("+" + "-------------+"*3 + "\n")
    else:
        word += str("|" + "             |"*3 + "\n")
    word += str(("|" + " {}    {}    {} |"*3 + "\n").format(*[x if x != 0 else " " for x in row]))
  word += str("+" + "-------------+"*3)
  screen.addstr(word)
  screen.refresh()
  sleep(0.1)

def checkSolved():
  for i in range(81):
    if not valid((i//9), (i%9), board[i//9][i%9]):
      return False
  return True

screen = curses.initscr()
if(fill(0)):
  print(checkSolved())
else:
  print('Sudoku Input Invalid')
curses.endwin()