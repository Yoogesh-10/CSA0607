# DAA Assignment - Question 84
# Topic: Backtracking
# Algorithm: Subset generation
# Time complexity: O(2^n)

def subsets(a):
 out=[]
 def dfs(i,path):
  out.append(path[:])
  for j in range(i,len(a)):
   path.append(a[j]);dfs(j+1,path);path.pop()
 dfs(0,[]);return out
print(subsets([1,2,3]))
