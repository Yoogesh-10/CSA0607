# DAA Assignment - Question 67
# Topic: Dynamic Programming
# Algorithm: Frog jump minimum cost
# Time complexity: O(n)

def frog(a):
 dp=[0]*len(a)
 for i in range(1,len(a)):dp[i]=dp[i-1]+abs(a[i]-a[i-1])
 return dp[-1]
print("Cost:",frog([10,20,30,10]))
