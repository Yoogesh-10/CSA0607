# DAA Assignment - Question 18
# Topic: Brute Force
# Algorithm: Pairwise closest distance
# Time complexity: O(n²)

def closest_pair_1d(a):
    best=None
    for i in range(len(a)):
      for j in range(i+1,len(a)):
        d=abs(a[i]-a[j])
        if best is None or d<best[0]:best=(d,(a[i],a[j]))
    return best
print(closest_pair_1d([1,8,3,12,4]))
