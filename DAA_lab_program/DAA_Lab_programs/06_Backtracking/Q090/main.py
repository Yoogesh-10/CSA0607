# DAA Assignment - Question 90
# Topic: Backtracking
# Algorithm: TSP backtracking
# Time complexity: O(n!)

def tsp(g):
 n=len(g);best=float("inf");bestpath=[]
 def dfs(u,visited,cost,path):
  nonlocal best,bestpath
  if len(path)==n:
   if g[u][0] and cost+g[u][0]<best:best=cost+g[u][0];bestpath=path+[0]
   return
  for v in range(n):
   if v not in visited and g[u][v]:
    dfs(v,visited|{v},cost+g[u][v],path+[v])
 dfs(0,{0},0,[0]);return best,bestpath
g=[[0,10,15,20],[10,0,35,25],[15,35,0,30],[20,25,30,0]]
print(tsp(g))
