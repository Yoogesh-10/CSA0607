# DAA Assignment - Question 9
# Topic: Introduction
# Algorithm: Binary search
# Time complexity: O(log n)

def binary_search(a,key):
    lo,hi=0,len(a)-1
    while lo<=hi:
        mid=(lo+hi)//2
        if a[mid]==key:return mid
        if a[mid]<key:lo=mid+1
        else:hi=mid-1
    return -1
a=sorted([3,4,6,-9,10,8,9,30]); key=10
print("Sorted:",a)
p=binary_search(a,key)
print(f"Element {key} found at position {p+1}" if p>=0 else "Not found")
