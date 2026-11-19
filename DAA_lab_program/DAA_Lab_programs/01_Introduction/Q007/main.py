# DAA Assignment - Question 7
# Topic: Introduction
# Algorithm: Unique elements preserving order
# Time complexity: O(n) time, O(n) space

def unique(a):
    seen=set(); out=[]
    for x in a:
        if x not in seen: seen.add(x); out.append(x)
    return out
a=[3,7,3,5,2,5,9,2]
print("Input:",a)
print("Unique:",unique(a))
