# DAA Assignment - Question 87
# Topic: Backtracking
# Algorithm: Graph coloring
# Time complexity: O(k^V)

def color_graph(g,k):
 n=len(g);c=[0]*n
 def dfs(v):
  if v==n:return True
  for x in range(1,k+1):
   if all(not g[v][u] or c[u]!=x for u in range(n)):
    c[v]=x
    if dfs(v+1):return True
    c[v]=0
  return False
 return dfs(0),c
g=[[0,1,1,0],[1,0,1,1],[1,1,0,1],[0,1,1,0]]
print(color_graph(g,3))
