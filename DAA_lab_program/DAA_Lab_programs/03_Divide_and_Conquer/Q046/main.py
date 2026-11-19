# DAA Assignment - Question 46
# Topic: Divide and Conquer
# Algorithm: Sort k-sorted array
# Time complexity: O(n log k)

import heapq
def sort_k(a,k):
 h=a[:k+1];heapq.heapify(h);out=[]
 for x in a[k+1:]:out.append(heapq.heappop(h));heapq.heappush(h,x)
 while h:out.append(heapq.heappop(h))
 return out
print(sort_k([2,1,4,3,6,5],2))
