# DAA Assignment - Question 65
# Topic: Dynamic Programming
# Algorithm: Triangle minimum path
# Time complexity: O(n²)

def triangle_min(t):
 dp=t[-1][:]
 for row in reversed(t[:-1]):
  dp=[row[i]+min(dp[i],dp[i+1]) for i in range(len(row))]
 return dp[0]
print(triangle_min([[2],[3,4],[6,5,7],[4,1,8,3]]))
