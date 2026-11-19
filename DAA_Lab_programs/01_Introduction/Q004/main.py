# DAA Assignment - Question 4
# Topic: Introduction
# Algorithm: Equal-value divisible index pairs
# Time complexity: O(n²)

def count_pairs(a,k):
    return sum(a[i]==a[j] and (i*j)%k==0 for i in range(len(a)) for j in range(i+1,len(a)))
a=[3,1,2,2,2,1,3]; k=2
print("Array:",a,"k =",k)
print("Pairs:",count_pairs(a,k))
