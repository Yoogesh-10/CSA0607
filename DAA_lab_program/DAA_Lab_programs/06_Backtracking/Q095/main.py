# DAA Assignment - Question 95
# Topic: Backtracking
# Algorithm: Knight tour existence demo
# Time complexity: O(8^(n²))

moves=[(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
def tour(n):
 b=[[-1]*n for _ in range(n)];b[0][0]=0
 def dfs(r,c,k):
  if k==n*n:return True
  for dr,dc in moves:
   nr,nc=r+dr,c+dc
   if 0<=nr<n and 0<=nc<n and b[nr][nc]<0:
    b[nr][nc]=k
    if dfs(nr,nc,k+1):return True
    b[nr][nc]=-1
  return False
 return dfs(0,0,1),b
ok,_=tour(5);print("5x5 tour found:",ok)
