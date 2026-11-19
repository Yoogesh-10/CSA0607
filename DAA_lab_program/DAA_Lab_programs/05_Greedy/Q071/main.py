# DAA Assignment - Question 71
# Topic: Greedy
# Algorithm: Greedy coin change
# Time complexity: O(k log k)

def change(coins,amount):
 out=[]
 for c in sorted(coins,reverse=True):
  q,amount=divmod(amount,c);out.extend([c]*q)
 return out if amount==0 else None
print(change([1,5,10,25],63))
