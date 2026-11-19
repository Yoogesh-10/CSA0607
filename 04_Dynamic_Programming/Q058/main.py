# DAA Assignment - Question 58
# Topic: Dynamic Programming
# Algorithm: Edit distance
# Time complexity: O(mn)

def edit(a,b):
 dp=[[0]*(len(b)+1) for _ in range(len(a)+1)]
 for i in range(len(a)+1):dp[i][0]=i
 for j in range(len(b)+1):dp[0][j]=j
 for i in range(1,len(a)+1):
  for j in range(1,len(b)+1):
   dp[i][j]=dp[i-1][j-1] if a[i-1]==b[j-1] else 1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
 return dp[-1][-1]
print("Distance:",edit("kitten","sitting"))
