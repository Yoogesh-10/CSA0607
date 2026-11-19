# DAA Assignment - Question 5
# Topic: Introduction
# Algorithm: Maximum element
# Time complexity: O(n)

def maximum(a):
    return max(a) if a else None
for a in ([1,2,3,4,5],[7,7,7],[-10,2,3,-4,5],[]):
    print(a,"->",maximum(a))
