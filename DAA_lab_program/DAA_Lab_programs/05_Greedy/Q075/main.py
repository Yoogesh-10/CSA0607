# DAA Assignment - Question 75
# Topic: Greedy
# Algorithm: Greedy set cover
# Time complexity: O(number of selections × sets)

def cover(U,S):
 uncovered=set(U);chosen=[]
 while uncovered:
  best=max(S,key=lambda s:len(set(s)&uncovered))
  gain=set(best)&uncovered
  if not gain:break
  chosen.append(best);uncovered-=gain
 return chosen
U=set(range(1,8));S=[{1,2,3},{2,4},{3,4,5,6},{4,5},{5,6,7},{6,7}]
print("Cover:",cover(U,S))
