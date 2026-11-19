# DAA Assignment - Question 62
# Topic: Dynamic Programming
# Algorithm: Matrix chain multiplication
# Time complexity: O(n³)

def mcm(p):
 n=len(p)-1;dp=[[0]*n for _ in range(n)]
 for L in range(2,n+1):
  for i in range(n-L+1):
   j=i+L-1;dp[i][j]=min(dp[i][k]+dp[k+1][j]+p[i]*p[k+1]*p[j+1] for k in range(i,j))
 return dp[0][n-1]
print("Min multiplications:",mcm([10,20,30,40]))
