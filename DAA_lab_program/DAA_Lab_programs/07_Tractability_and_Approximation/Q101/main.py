# DAA Assignment - Question 101
# Topic: Tractability and Approximation
# Algorithm: First fit bin packing
# Time complexity: O(n²)

def first_fit(items,capacity):
 bins=[]
 for x in items:
  for b in bins:
   if sum(b)+x<=capacity:b.append(x);break
  else:bins.append([x])
 return bins
print(first_fit([4,8,1,4,2,1],10))
