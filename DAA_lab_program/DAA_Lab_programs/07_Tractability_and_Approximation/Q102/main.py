# DAA Assignment - Question 102
# Topic: Tractability and Approximation
# Algorithm: Maximum cut exhaustive
# Time complexity: O(2^V·E)

from itertools import product
edges=[(0,1,2),(0,2,1),(1,2,3),(1,3,4),(2,3,2)]
def maxcut(n,edges):
 best=0;side=None
 for bits in product([0,1],repeat=n):
  w=sum(x for u,v,x in edges if bits[u]!=bits[v])
  if w>best:best=w;side=bits
 return best,side
print("Optimal cut:",maxcut(4,edges))
