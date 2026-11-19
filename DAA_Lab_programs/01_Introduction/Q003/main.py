# DAA Assignment - Question 3
# Topic: Introduction
# Algorithm: Sum of squared distinct counts
# Time complexity: O(n²)

def sum_sq_distinct(arr):
    total=0
    for i in range(len(arr)):
        seen=set()
        for j in range(i,len(arr)):
            seen.add(arr[j]); total += len(seen)**2
    return total
a=[1,2,1]
print("Array:",a)
print("Result:",sum_sq_distinct(a))
