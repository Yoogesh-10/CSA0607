# DAA Assignment - Question 81
# Topic: Backtracking
# Algorithm: N-Queens
# Time complexity: O(n!)

def nqueens(n):
 cols=set();d1=set();d2=set();board=[];solutions=[]
 def dfs(r):
  if r==n:solutions.append(board[:]);return
  for c in range(n):
   if c in cols or r-c in d1 or r+c in d2:continue
   cols.add(c);d1.add(r-c);d2.add(r+c);board.append(c)
   dfs(r+1)
   board.pop();cols.remove(c);d1.remove(r-c);d2.remove(r+c)
 dfs(0);return solutions
print("Solutions for 4 queens:",len(nqueens(4)),nqueens(4))
