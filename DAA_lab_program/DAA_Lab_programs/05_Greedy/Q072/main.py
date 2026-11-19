# DAA Assignment - Question 72
# Topic: Greedy
# Algorithm: Huffman coding
# Time complexity: O(n log n)

import heapq
def huffman(freq):
 h=[[w,[ch,""]] for ch,w in freq.items()];heapq.heapify(h)
 while len(h)>1:
  a=heapq.heappop(h);b=heapq.heappop(h)
  for pair in a[1:]:pair[1]="0"+pair[1]
  for pair in b[1:]:pair[1]="1"+pair[1]
  heapq.heappush(h,[a[0]+b[0]]+a[1:]+b[1:])
 return dict(h[0][1:])
print(huffman({"a":5,"b":9,"c":12,"d":13,"e":16,"f":45}))
