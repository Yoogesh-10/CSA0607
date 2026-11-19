# DAA Assignment - Question 14
# Topic: Brute Force
# Algorithm: Linear search
# Time complexity: O(n)

def linear_search(a,x):
    for i,v in enumerate(a):
        if v==x:return i
    return -1
a=[4,7,2,9,5]; x=9
print("Index:",linear_search(a,x))
