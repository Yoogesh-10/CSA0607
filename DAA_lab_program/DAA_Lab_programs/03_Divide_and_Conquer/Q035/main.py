# DAA Assignment - Question 35
# Topic: Divide and Conquer
# Algorithm: Count inversions
# Time complexity: O(n log n)

def count_inv(a):
 if len(a)<2:return a,0
 m=len(a)//2; l,x=count_inv(a[:m]);r,y=count_inv(a[m:]);z=[];i=j=0;c=x+y
 while i<len(l) and j<len(r):
  if l[i]<=r[j]:z.append(l[i]);i+=1
  else:z.append(r[j]);j+=1;c+=len(l)-i
 return z+l[i:]+r[j:],c
print("Inversions:",count_inv([2,4,1,3,5])[1])
