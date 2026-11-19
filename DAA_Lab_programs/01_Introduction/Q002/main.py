# DAA Assignment - Question 2
# Topic: Introduction
# Algorithm: Common elements count
# Time complexity: O(n+m)

def common_counts(a,b):
    sb=set(b); sa=set(a)
    return [sum(x in sb for x in a), sum(x in sa for x in b)]
a=[2,3,2]; b=[1,2]
print("Arrays:",a,b)
print("Counts:",common_counts(a,b))
