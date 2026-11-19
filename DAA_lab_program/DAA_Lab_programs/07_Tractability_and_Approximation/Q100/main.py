# DAA Assignment - Question 100
# Topic: Tractability and Approximation
# Algorithm: Greedy set cover approximation
# Time complexity: O(sets·universe)

U=set(range(1,8));S=[{1,2,3},{2,4},{3,4,5,6},{4,5},{5,6,7},{6,7}]
def greedy(U,S):
 uncovered=U.copy();chosen=[]
 while uncovered:
  s=max(S,key=lambda x:len(x&uncovered))
  if not s&uncovered:break
  chosen.append(s);uncovered-=s
 return chosen
print("Greedy:",greedy(U,S))
