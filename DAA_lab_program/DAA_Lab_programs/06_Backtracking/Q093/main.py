# DAA Assignment - Question 93
# Topic: Backtracking
# Algorithm: Balanced parentheses
# Time complexity: O(Catalan(n))

def parens(n):
 out=[]
 def dfs(s,o,c):
  if len(s)==2*n:out.append(s);return
  if o<n:dfs(s+"(",o+1,c)
  if c<o:dfs(s+")",o,c+1)
 dfs("",0,0);return out
print(parens(3))
