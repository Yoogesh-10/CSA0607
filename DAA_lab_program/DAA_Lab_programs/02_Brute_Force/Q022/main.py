# DAA Assignment - Question 22
# Topic: Brute Force
# Algorithm: Maximum subarray brute force
# Time complexity: O(n²)

def max_subarray(a):
    best=-float("inf")
    for i in range(len(a)):
      total=0
      for j in range(i,len(a)):
        total+=a[j]; best=max(best,total)
    return best
print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))
