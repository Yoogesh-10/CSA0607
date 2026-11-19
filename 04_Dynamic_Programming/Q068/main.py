# DAA Assignment - Question 68
# Topic: Dynamic Programming
# Algorithm: Best time stock one transaction
# Time complexity: O(n)

def max_profit(prices):
 low=float("inf");best=0
 for p in prices:low=min(low,p);best=max(best,p-low)
 return best
print("Profit:",max_profit([7,1,5,3,6,4]))
