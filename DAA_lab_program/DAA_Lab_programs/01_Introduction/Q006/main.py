# DAA Assignment - Question 6
# Topic: Introduction
# Algorithm: Sort then maximum
# Time complexity: O(n log n)

def sort_then_max(a):
    if not a:return None
    a=sorted(a); return a[-1]
for a in ([],[5],[3,3,3,3]):
    print(a,"->",sort_then_max(a))
