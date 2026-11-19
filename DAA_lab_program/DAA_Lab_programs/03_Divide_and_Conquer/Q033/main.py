# DAA Assignment - Question 33
# Topic: Divide and Conquer
# Algorithm: Quick sort
# Time complexity: Average O(n log n)

def quicksort(a):
 if len(a)<=1:return a
 p=a[len(a)//2]
 return quicksort([x for x in a if x<p])+[x for x in a if x==p]+quicksort([x for x in a if x>p])
print(quicksort([7,2,9,1,5,3]))
