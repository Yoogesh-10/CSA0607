# DAA Assignment - Question 79
# Topic: Greedy
# Algorithm: Greedy coloring
# Time complexity: O(V²)

def greedy_color(g):
 color={}
 for v in range(len(g)):
  used={color[u] for u in g[v] if u in color};c=0
  while c in used:c+=1
  color[v]=c
 return color
g=[[1,2],[0,2],[0,1,3],[2]]
print(greedy_color(g))
