# DAA Assignment - Question 55
# Topic: Dynamic Programming
# Algorithm: Coin change count
# Time complexity: O(amount·coins)

def count_ways(coins,amount):
 dp=[0]*(amount+1);dp[0]=1
 for c in coins:
  for x in range(c,amount+1):dp[x]+=dp[x-c]
 return dp[amount]
print("Ways:",count_ways([1,2,5],5))
