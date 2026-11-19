# DAA Assignment - Question 70
# Topic: Greedy
# Algorithm: Fractional knapsack
# Time complexity: O(n log n)

def frac(items,cap):
 items=sorted(items,key=lambda x:x[1]/x[0],reverse=True);value=0;take=[]
 for w,v in items:
  if cap<=0:break
  x=min(w,cap);value+=v*x/w;cap-=x;take.append((w,x))
 return value,take
print(frac([(10,60),(20,100),(30,120)],50))
