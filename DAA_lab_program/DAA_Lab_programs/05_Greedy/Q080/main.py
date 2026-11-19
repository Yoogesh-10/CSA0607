# DAA Assignment - Question 80
# Topic: Greedy
# Algorithm: Optimal merge pattern
# Time complexity: O(n log n)

import heapq
def merge_cost(files):
 h=files[:];heapq.heapify(h);cost=0
 while len(h)>1:
  a=heapq.heappop(h);b=heapq.heappop(h);s=a+b;cost+=s;heapq.heappush(h,s)
 return cost
print("Total merge cost:",merge_cost([5,10,20,30]))
