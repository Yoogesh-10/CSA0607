# DAA Assignment - Question 19
# Topic: Brute Force
# Algorithm: Subset sum brute force
# Time complexity: O(2^n)

def subset_sum(a,target):
    n=len(a)
    for mask in range(1<<n):
      chosen=[a[i] for i in range(n) if mask>>i&1]
      if sum(chosen)==target:return chosen
    return None
print("Subset:",subset_sum([3,5,7,2],10))
