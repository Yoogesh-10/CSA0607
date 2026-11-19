# DAA Assignment - Question 66
# Topic: Dynamic Programming
# Algorithm: Maximal square
# Time complexity: O(mn)

def maximal_square(mat):
 if not mat:return 0
 dp=[[0]*(len(mat[0])+1) for _ in mat];best=0
 for i in range(1,len(dp)):
  for j in range(1,len(dp[0])):
   if mat[i-1][j-1]:dp[i][j]=1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]);best=max(best,dp[i][j])
 return best*best
print("Area:",maximal_square([[1,0,1,0,0],[1,0,1,1,1],[1,1,1,1,1],[1,0,0,1,0]]))
