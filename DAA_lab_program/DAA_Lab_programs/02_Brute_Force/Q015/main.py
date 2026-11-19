# DAA Assignment - Question 15
# Topic: Brute Force
# Algorithm: Two sum brute force
# Time complexity: O(n²)

def two_sum(a,target):
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]+a[j]==target:return [i,j]
    return []
a=[2,7,11,15]; print("Pair:",two_sum(a,9))
