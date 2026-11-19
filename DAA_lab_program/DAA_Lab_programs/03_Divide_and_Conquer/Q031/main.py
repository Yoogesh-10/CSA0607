# DAA Assignment - Question 31
# Topic: Divide and Conquer
# Algorithm: Binary search recursive
# Time complexity: O(log n)

def bs(a,x,l=0,r=None):
    if r is None:r=len(a)-1
    if l>r:return -1
    m=(l+r)//2
    if a[m]==x:return m
    return bs(a,x,m+1,r) if a[m]<x else bs(a,x,l,m-1)
a=[1,3,5,7,9];print("Index:",bs(a,7))
