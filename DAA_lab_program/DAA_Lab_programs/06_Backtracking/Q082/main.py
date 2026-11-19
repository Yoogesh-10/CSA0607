# DAA Assignment - Question 82
# Topic: Backtracking
# Algorithm: Maze path
# Time complexity: O(4^(mn)) worst-case

def solve_maze(m):
 n=len(m);path=[]
 def dfs(r,c):
  if r==n-1 and c==n-1:path.append((r,c));return True
  if r<0 or c<0 or r>=n or c>=n or not m[r][c]:return False
  m[r][c]=0;path.append((r,c))
  if dfs(r+1,c) or dfs(r,c+1) or dfs(r-1,c) or dfs(r,c-1):return True
  path.pop();return False
 return path if dfs(0,0) else None
print(solve_maze([[1,1,0],[1,1,1],[0,1,1]]))
