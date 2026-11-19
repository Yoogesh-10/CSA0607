# DAA Assignment - Question 36
# Topic: Divide and Conquer
# Algorithm: Closest pair 1D after sort
# Time complexity: O(n log n)

def closest(a):
 a=sorted(a)
 return min((a[i+1]-a[i],a[i],a[i+1]) for i in range(len(a)-1))
print(closest([2,10,5,7,1]))
