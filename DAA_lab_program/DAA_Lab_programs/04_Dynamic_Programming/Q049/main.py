# DAA Assignment - Question 49
# Topic: Dynamic Programming
# Algorithm: House robber linear
# Time complexity: O(n)

def rob(a):
 prev2=prev1=0
 for x in a:prev2,prev1=prev1,max(prev1,prev2+x)
 return prev1
print("Maximum:",rob([2,7,9,3,1]))
