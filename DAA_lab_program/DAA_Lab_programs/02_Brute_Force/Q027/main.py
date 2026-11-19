# DAA Assignment - Question 27
# Topic: Brute Force
# Algorithm: All pairs differences
# Time complexity: O(n²)

def pair_diffs(a):
    return [(a[i],a[j],a[j]-a[i]) for i in range(len(a)) for j in range(i+1,len(a))]
print(pair_diffs([1,4,6]))
