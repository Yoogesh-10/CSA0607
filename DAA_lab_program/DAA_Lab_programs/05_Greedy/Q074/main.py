# DAA Assignment - Question 74
# Topic: Greedy
# Algorithm: Dijkstra shortest paths
# Time complexity: O((V+E) log V)

import heapq
def dijkstra(g,s):
 d={v:float("inf") for v in g};d[s]=0;h=[(0,s)]
 while h:
  dist,u=heapq.heappop(h)
  if dist!=d[u]:continue
  for v,w in g[u].items():
   if dist+w<d[v]:d[v]=dist+w;heapq.heappush(h,(d[v],v))
 return d
g={0:{1:4,2:1},1:{3:1},2:{1:2,3:5},3:{}}
print(dijkstra(g,0))
