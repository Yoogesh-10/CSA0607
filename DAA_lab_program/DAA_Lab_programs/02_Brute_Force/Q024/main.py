# DAA Assignment - Question 24
# Topic: Brute Force
# Algorithm: Check duplicate by pairs
# Time complexity: O(n²)

def has_duplicate(a):
    for i in range(len(a)):
      for j in range(i+1,len(a)):
       if a[i]==a[j]:return True
    return False
print(has_duplicate([1,2,3,1]))
