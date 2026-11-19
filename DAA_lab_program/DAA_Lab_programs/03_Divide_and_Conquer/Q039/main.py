# DAA Assignment - Question 39
# Topic: Divide and Conquer
# Algorithm: Ternary search
# Time complexity: O(log n)

def ternary(a,x):
 l,r=0,len(a)-1
 while l<=r:
  m1=l+(r-l)//3;m2=r-(r-l)//3
  if a[m1]==x:return m1
  if a[m2]==x:return m2
  if x<a[m1]:r=m1-1
  elif x>a[m2]:l=m2+1
  else:l=m1+1;r=m2-1
 return -1
print(ternary([1,2,4,6,8,9],8))
