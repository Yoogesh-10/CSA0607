# DAA Assignment - Question 8
# Topic: Introduction
# Algorithm: Bubble sort
# Time complexity: O(n²)

def bubble_sort(a):
    a=a[:]
    for i in range(len(a)):
        swapped=False
        for j in range(0,len(a)-i-1):
            if a[j]>a[j+1]: a[j],a[j+1]=a[j+1],a[j]; swapped=True
        if not swapped: break
    return a
a=[5,1,4,2,8]
print("Sorted:",bubble_sort(a))
