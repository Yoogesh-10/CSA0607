# DAA Assignment - Question 83
# Topic: Backtracking
# Algorithm: Sudoku solver
# Time complexity: O(9^(empty cells))

def solve(board):
 def find():
  for r in range(9):
   for c in range(9):
    if board[r][c]==0:return r,c
  return None
 def valid(r,c,x):
  return all(board[r][j]!=x for j in range(9)) and all(board[i][c]!=x for i in range(9)) and all(board[i][j]!=x for i in range(r//3*3,r//3*3+3) for j in range(c//3*3,c//3*3+3))
 p=find()
 if not p:return True
 r,c=p
 for x in range(1,10):
  if valid(r,c,x):
   board[r][c]=x
   if solve(board):return True
   board[r][c]=0
 return False
b=[[5,3,0,0,7,0,0,0,0],[6,0,0,1,9,5,0,0,0],[0,9,8,0,0,0,0,6,0],[8,0,0,0,6,0,0,0,3],[4,0,0,8,0,3,0,0,1],[7,0,0,0,2,0,0,0,6],[0,6,0,0,0,0,2,8,0],[0,0,0,4,1,9,0,0,5],[0,0,0,0,8,0,0,7,9]]
solve(b);print("Solved first row:",b[0])
