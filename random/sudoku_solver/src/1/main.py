"""
Giving a board in a 2D array form it will loop through line by line
and look if the squre is empty or has some value in it

"""
board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

# this is the backtrack algorithm
def solve(board):
  
  find = find_empty(board)
  if not find:
    return True
  else:
    row, column = find

  for i in range(1,10):
    if is_valid(board, i, (row, column)):
      board[row][column] = i

      if solve(board):
        return True

        board[row][column] = 0

  return False

def is_valid(board, number, position):
  
  # check row
  ## for each column in the given row
  for column in range(len(bo[0])): # it could be hardcoded 9 but 0 in case the board could be bigger
    if board[pos[0][column]] == number and pos[0] != column:
      return False # cuz we find duplicate

  # check column
  ## do it vertically
  for row in range(len(board)):
    if board[row][pos[1]] == num and pos[0] != row:
      return False # cuz we find duplicate

  # check grid
  ## column
  box_x = po[1] // 3
  box_y = po[0] // 3

  # make sure we don't have the same element twice
  for i in range(box_y*3, box_y*3 + 3):
    for j in range(box_y*3, box_y*3 + 3):
      if board[i][j] == num and (i,j) != pos:
        return False # cuz we find duplicate

  return True # if we get it through all of these checks we find a valid position

def print_board(board):
  for horizontal_row in range(len(board)):
    if horizontal_row % 3 == 0 and horizontal_row != 0:
      print("- - - - - - - - - - - -")
    
    # lenght of the row
    for position_in_row in range(len(board)):
      if position_in_row % 3 == 0 and position_in_row != 0:
        print(" | ", end="") # end="" --> it does not print a \n

      if position_in_row == 8:
        print(board[horizontal_row][position_in_row])
      else:
        print(str(board[horizontal_row][position_in_row]) + " ", end="")

def find_empty(board):
  for row in range(len(board)):
    # lenght of each row
    for column in range (len(board[0])):
      if board[row][column] == 0:
        return (row, column) # return a tuple of (row, column) y x


print_board(board)
solve(board)
print("--------------------------------")
print_board(board)