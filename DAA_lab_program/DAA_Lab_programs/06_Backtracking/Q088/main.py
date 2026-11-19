# DAA Assignment - Question 88
# Topic: Backtracking
# Algorithm: Hamiltonian cycle
# Time complexity: O(V!)

def ham_cycle(g):
 n=len(g);path=[0]
 def dfs(v):
  if len(path)==n:return g[v][0]==1
  for u in range(1,n):
   if u not in path and g[v][u]:
    path.append(u)
    if dfs(u):return True
    path.pop()
  return False
 return path+[0] if dfs(0) else None
g=[[0,1,1,1],[1,0,1,0],[1,1,0,1],[1,0,1,0]]
print("Cycle:",ham_cycle(g))
