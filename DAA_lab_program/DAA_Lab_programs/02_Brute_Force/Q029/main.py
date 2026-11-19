# DAA Assignment - Question 29
# Topic: Brute Force
# Algorithm: Brute-force knapsack
# Time complexity: O(2^n)

def knapsack(items,capacity):
    best=(0,[])
    for mask in range(1<<len(items)):
      weight=value=0; chosen=[]
      for i,(w,v) in enumerate(items):
       if mask>>i&1:weight+=w;value+=v;chosen.append(i)
      if weight<=capacity and value>best[0]:best=(value,chosen)
    return best
print(knapsack([(2,3),(3,4),(4,5)],5))
