# DAA Assignment - Question 61
# Topic: Dynamic Programming
# Algorithm: Maximum subarray Kadane
# Time complexity: O(n)

def kadane(a):
 best=cur=a[0]
 for x in a[1:]:cur=max(x,cur+x);best=max(best,cur)
 return best
print("Max sum:",kadane([-2,1,-3,4,-1,2,1,-5,4]))
