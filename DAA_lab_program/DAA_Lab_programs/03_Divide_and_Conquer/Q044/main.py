# DAA Assignment - Question 44
# Topic: Divide and Conquer
# Algorithm: Recursive gcd
# Time complexity: O(log min(a,b))

def gcd(a,b):
 return a if b==0 else gcd(b,a%b)
print("GCD:",gcd(48,18))
