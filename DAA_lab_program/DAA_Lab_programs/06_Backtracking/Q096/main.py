# DAA Assignment - Question 96
# Topic: Backtracking
# Algorithm: Partition into k subsets
# Time complexity: O(k^n)

def partition_k(a,k):
 buckets=[0]*k
 def dfs(i):
  if i==len(a):return max(buckets)-min(buckets)==0
  for j in range(k):
   buckets[j]+=a[i]
   if dfs(i+1):return True
   buckets[j]-=a[i]
   if buckets[j]==0:break
  return False
 return sum(a)%k==0 and dfs(0)
print(partition_k([4,3,2,3,5,2,1],4))
