# DAA Assignment - Question 34
# Topic: Divide and Conquer
# Algorithm: Find min and max divide-conquer
# Time complexity: O(n)

def minmax(a):
 if len(a)==1:return a[0],a[0]
 m=len(a)//2; x=minmax(a[:m]); y=minmax(a[m:])
 return min(x[0],y[0]),max(x[1],y[1])
print(minmax([8,2,9,4,1,7]))
