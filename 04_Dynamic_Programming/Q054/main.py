# DAA Assignment - Question 54
# Topic: Dynamic Programming
# Algorithm: Coin change minimum
# Time complexity: O(amount·coins)

def min_coins(coins,amount):
 dp=[amount+1]*(amount+1);dp[0]=0
 for c in coins:
  for x in range(c,amount+1):dp[x]=min(dp[x],dp[x-c]+1)
 return dp[amount] if dp[amount]<=amount else -1
print(min_coins([1,2,5],11))
