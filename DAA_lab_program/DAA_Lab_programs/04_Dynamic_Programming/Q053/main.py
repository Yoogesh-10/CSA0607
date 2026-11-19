# DAA Assignment - Question 53
# Topic: Dynamic Programming
# Algorithm: 0/1 knapsack
# Time complexity: O(nW)

def knapsack(w,v,cap):
 dp=[0]*(cap+1)
 for wt,val in zip(w,v):
  for c in range(cap,wt-1,-1):dp[c]=max(dp[c],dp[c-wt]+val)
 return dp[cap]
print("Best value:",knapsack([2,3,4],[3,4,5],5))
