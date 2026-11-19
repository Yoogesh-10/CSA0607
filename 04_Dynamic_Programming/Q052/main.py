# DAA Assignment - Question 52
# Topic: Dynamic Programming
# Algorithm: Minimum path sum
# Time complexity: O(mn)

def min_path(g):
 dp=g[0][:]
 for i in range(1,len(g)):dp[0]+=g[i][0]
 for j in range(1,len(dp)):dp[j]+=dp[j-1]
 for i in range(1,len(g)):
  for j in range(1,len(dp)):dp[j]=g[i][j]+min(dp[j],dp[j-1])
 return dp[-1]
print(min_path([[1,3,1],[1,5,1],[4,2,1]]))
