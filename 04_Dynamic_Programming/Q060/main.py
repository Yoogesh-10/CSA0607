# DAA Assignment - Question 60
# Topic: Dynamic Programming
# Algorithm: Partition equal subset
# Time complexity: O(n·sum)

def can_partition(a):
 total=sum(a)
 if total%2:return False
 return subset_sum(a,total//2)
def subset_sum(a,t):
 dp={0}
 for x in a:dp|={s+x for s in dp}
 return t in dp
print(can_partition([1,5,11,5]))
