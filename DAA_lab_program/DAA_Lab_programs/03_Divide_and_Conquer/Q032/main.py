# DAA Assignment - Question 32
# Topic: Divide and Conquer
# Algorithm: Merge sort
# Time complexity: O(n log n)

def merge_sort(a):
 if len(a)<2:return a
 m=len(a)//2
 x,y=merge_sort(a[:m]),merge_sort(a[m:]); z=[]
 while x and y:z.append(x.pop(0) if x[0]<y[0] else y.pop(0))
 return z+x+y
print(merge_sort([9,4,6,2,7,1]))
