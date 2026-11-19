# DAA Assignment - Question 92
# Topic: Backtracking
# Algorithm: Generate subsets containing target
# Time complexity: O(2^n)

def contain(a,x):
 return [s for s in subsets(a) if x in s]
def subsets(a):
 out=[]
 def dfs(i,p):
  if i==len(a):out.append(p[:]);return
  dfs(i+1,p);p.append(a[i]);dfs(i+1,p);p.pop()
 dfs(0,[]);return out
print(contain([2,3,4,5],3))
