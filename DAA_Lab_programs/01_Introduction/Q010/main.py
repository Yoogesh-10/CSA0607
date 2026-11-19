# DAA Assignment - Question 10
# Topic: Introduction
# Algorithm: Merge sort
# Time complexity: O(n log n)

def merge_sort(a):
    if len(a)<=1:return a
    m=len(a)//2; left=merge_sort(a[:m]); right=merge_sort(a[m:])
    out=[]
    while left and right: out.append(left.pop(0) if left[0]<=right[0] else right.pop(0))
    return out+left+right
a=[5,2,8,1,3]
print("Sorted:",merge_sort(a))
