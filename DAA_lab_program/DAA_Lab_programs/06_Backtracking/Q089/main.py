# DAA Assignment - Question 89
# Topic: Backtracking
# Algorithm: Rat in maze
# Time complexity: O(4^(n²))

def paths(m):
 n=len(m);res=[]
 def dfs(r,c,p):
  if r==n-1 and c==n-1:res.append(p);return
  for dr,dc,ch in [(1,0,"D"),(0,1,"R"),(-1,0,"U"),(0,-1,"L")]:
   nr,nc=r+dr,c+dc
   if 0<=nr<n and 0<=nc<n and m[nr][nc]==1:
    m[nr][nc]=0;dfs(nr,nc,p+ch);m[nr][nc]=1
 m[0][0]=0;dfs(0,0,"");return res
print(paths([[1,1,0],[1,1,1],[0,1,1]]))
