# DAA Assignment - Question 85
# Topic: Backtracking
# Algorithm: Permutations backtracking
# Time complexity: O(n·n!)

def permutations(a):
 out=[]
 def dfs(path,used):
  if len(path)==len(a):out.append(path[:]);return
  for i,x in enumerate(a):
   if not used[i]:
    used[i]=1;path.append(x);dfs(path,used);path.pop();used[i]=0
 dfs([], [0]*len(a));return out
print(permutations([1,2,3]))
