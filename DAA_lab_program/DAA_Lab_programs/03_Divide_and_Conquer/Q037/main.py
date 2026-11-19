# DAA Assignment - Question 37
# Topic: Divide and Conquer
# Algorithm: Exponentiation by squaring
# Time complexity: O(log n)

def power(x,n):
 if n==0:return 1
 y=power(x,n//2)
 return y*y if n%2==0 else x*y*y
print("2^10 =",power(2,10))
