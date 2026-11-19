# DAA Assignment - Question 73
# Topic: Greedy
# Algorithm: Minimum spanning tree Kruskal
# Time complexity: O(E log E)

def kruskal(n,edges):
 parent=list(range(n))
 def find(x):
  while parent[x]!=x:parent[x]=parent[parent[x]];x=parent[x]
  return x
 out=[];cost=0
 for w,u,v in sorted(edges):
  a,b=find(u),find(v)
  if a!=b:parent[a]=b;out.append((u,v,w));cost+=w
 return out,cost
print(kruskal(4,[(1,0,1),(2,1,2),(3,0,2),(4,2,3)]))
