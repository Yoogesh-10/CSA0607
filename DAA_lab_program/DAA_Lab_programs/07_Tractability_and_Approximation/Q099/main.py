# DAA Assignment - Question 99
# Topic: Tractability and Approximation
# Algorithm: Vertex cover approximation vs exact
# Time complexity: Approx O(E), exact exponential

from itertools import combinations
E=[(1,2),(1,3),(2,3),(3,4),(4,5)]
def approx(edges):
 cover=set()
 for u,v in edges:
  if u not in cover and v not in cover:cover|={u,v}
 return cover
def exact(edges,vertices):
 for k in range(len(vertices)+1):
  for s in combinations(vertices,k):
   if all(u in s or v in s for u,v in edges):return set(s)
print("Approx:",approx(E));print("Exact:",exact(E,[1,2,3,4,5]))
