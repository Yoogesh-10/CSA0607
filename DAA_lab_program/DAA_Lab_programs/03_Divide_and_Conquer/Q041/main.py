# DAA Assignment - Question 41
# Topic: Divide and Conquer
# Algorithm: Majority divide conquer
# Time complexity: O(n log n)

def majority(a):
 if not a:return None
 if len(a)==1:return a[0]
 m=len(a)//2;x=majority(a[:m]);y=majority(a[m:])
 for c in (x,y):
  if c is not None and a.count(c)>len(a)//2:return c
 return None
print(majority([3,3,4,3,2,3,3]))
