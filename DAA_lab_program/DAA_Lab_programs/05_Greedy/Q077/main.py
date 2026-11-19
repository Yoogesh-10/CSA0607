# DAA Assignment - Question 77
# Topic: Greedy
# Algorithm: Job sequencing deadlines
# Time complexity: O(nD)

def schedule(jobs):
 jobs=sorted(jobs,key=lambda x:x[2],reverse=True);slots=[None]*max(j[1] for j in jobs);profit=0
 for name,d,p in jobs:
  for t in range(min(d,len(slots))-1,-1,-1):
   if slots[t] is None:slots[t]=name;profit+=p;break
 return slots,profit
print(schedule([("a",2,100),("b",1,19),("c",2,27),("d",1,25),("e",3,15)]))
