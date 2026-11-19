# DAA Assignment - Question 94
# Topic: Backtracking
# Algorithm: Combination n choose k
# Time complexity: O(C(n,k))

def combos(n,k):
 out=[]
 def dfs(start,p):
  if len(p)==k:out.append(p[:]);return
  for x in range(start,n+1):p.append(x);dfs(x+1,p);p.pop()
 dfs(1,[]);return out
print(combos(4,2))
