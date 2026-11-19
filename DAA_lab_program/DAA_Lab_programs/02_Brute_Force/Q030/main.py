# DAA Assignment - Question 30
# Topic: Brute Force
# Algorithm: Exhaustive graph coloring
# Time complexity: O(k^n)

def colorable(graph,k):
    n=len(graph); colors=[0]*n
    def check(v,c):
      return all(not graph[v][u] or colors[u]!=c for u in range(v))
    def dfs(v):
      if v==n:return True
      for c in range(1,k+1):
       if check(v,c):colors[v]=c
       if colors[v]==c and dfs(v+1):return True
       colors[v]=0
      return False
    return dfs(0),colors
g=[[0,1,1],[1,0,1],[1,1,0]]
print("3-colorable:",colorable(g,3))
