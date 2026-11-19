# DAA Assignment - Question 42
# Topic: Divide and Conquer
# Algorithm: Recursive sum
# Time complexity: O(n)

def total(a):
 if not a:return 0
 return a[0]+total(a[1:])
print(total([4,7,2,9]))
