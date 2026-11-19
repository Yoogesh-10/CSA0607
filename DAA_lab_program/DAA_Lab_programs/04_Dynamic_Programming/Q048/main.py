# DAA Assignment - Question 48
# Topic: Dynamic Programming
# Algorithm: Climbing stairs
# Time complexity: O(n)

def ways(n):
 a,b=1,1
 for _ in range(2,n+1):a,b=b,a+b
 return b
print("Ways for 4 steps:",ways(4))
