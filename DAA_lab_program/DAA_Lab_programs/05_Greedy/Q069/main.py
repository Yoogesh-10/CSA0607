# DAA Assignment - Question 69
# Topic: Greedy
# Algorithm: Activity selection
# Time complexity: O(n log n)

def select(a):
 a=sorted(a,key=lambda x:x[1]);out=[];end=-1
 for s,e in a:
  if s>=end:out.append((s,e));end=e
 return out
print(select([(1,3),(2,4),(3,5),(0,6),(5,7),(8,9)]))
