# DAA Assignment - Question 78
# Topic: Greedy
# Algorithm: Prim MST
# Time complexity: O(E log V)

import heapq
def prim(g,start):
 seen={start};h=[]
 for v,w in g[start]:heapq.heappush(h,(w,start,v))
 mst=[];cost=0
 while h:
  w,u,v=heapq.heappop(h)
  if v in seen:continue
  seen.add(v);mst.append((u,v,w));cost+=w
  for x,wx in g[v]:
   if x not in seen:heapq.heappush(h,(wx,v,x))
 return mst,cost
g={0:[(1,1),(2,4)],1:[(0,1),(2,2),(3,5)],2:[(0,4),(1,2),(3,1)],3:[(1,5),(2,1)]}
print(prim(g,0))
