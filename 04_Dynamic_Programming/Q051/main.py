# DAA Assignment - Question 51
# Topic: Dynamic Programming
# Algorithm: Unique paths grid
# Time complexity: O(mn)

def paths(m,n):
 dp=[1]*n
 for _ in range(m-1):
  for j in range(1,n):dp[j]+=dp[j-1]
 return dp[-1]
print("7x3 paths:",paths(7,3))
