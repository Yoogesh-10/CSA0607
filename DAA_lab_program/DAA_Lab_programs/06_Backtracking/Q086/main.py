# DAA Assignment - Question 86
# Topic: Backtracking
# Algorithm: Combination sum
# Time complexity: Exponential

def combination_sum(a,target):
 out=[]
 def dfs(i,remain,path):
  if remain==0:out.append(path[:]);return
  if remain<0:return
  for j in range(i,len(a)):
   path.append(a[j]);dfs(j,remain-a[j],path);path.pop()
 dfs(0,target,[]);return out
print(combination_sum([2,3,6,7],7))
