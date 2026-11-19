# DAA Assignment - Question 40
# Topic: Divide and Conquer
# Algorithm: Peak element
# Time complexity: O(log n)

def peak(a):
 l,r=0,len(a)-1
 while l<r:
  m=(l+r)//2
  if a[m]<a[m+1]:l=m+1
  else:r=m
 return l
a=[1,3,5,4,2];i=peak(a);print("Peak:",a[i],"index",i)
