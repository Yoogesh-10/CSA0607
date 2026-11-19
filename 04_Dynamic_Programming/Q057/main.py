# DAA Assignment - Question 57
# Topic: Dynamic Programming
# Algorithm: Longest increasing subsequence
# Time complexity: O(n log n)

def lis(a):
 dp=[]
 for x in a:
  i=0
  while i<len(dp) and dp[i]<x:i+=1
  if i==len(dp):dp.append(x)
  else:dp[i]=x
 return len(dp)
print("LIS length:",lis([10,9,2,5,3,7,101,18]))
