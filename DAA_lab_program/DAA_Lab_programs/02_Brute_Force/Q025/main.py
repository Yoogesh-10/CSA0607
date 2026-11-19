# DAA Assignment - Question 25
# Topic: Brute Force
# Algorithm: Majority element brute force
# Time complexity: O(n²)

def majority(a):
    for x in a:
      if sum(v==x for v in a)>len(a)//2:return x
    return None
print(majority([2,2,1,2,3,2,2]))
