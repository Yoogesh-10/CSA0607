# DAA Assignment - Question 59
# Topic: Dynamic Programming
# Algorithm: Subset sum DP
# Time complexity: O(n·sum)

def subset_sum(a,t):
 dp={0}
 for x in a:dp|={s+x for s in dp}
 return t in dp
print("Target 9 possible:",subset_sum([3,34,4,12,5,2],9))
