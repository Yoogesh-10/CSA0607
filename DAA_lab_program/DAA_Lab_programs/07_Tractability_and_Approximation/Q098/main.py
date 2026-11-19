# DAA Assignment - Question 98
# Topic: Tractability and Approximation
# Algorithm: 3-SAT exhaustive solver
# Time complexity: O(2^n) brute-force

from itertools import product
clauses=[[(1,True),(2,True),(3,False)],[(1,False),(2,True),(4,True)],[(3,True),(4,False),(5,True)]]
def sat(clauses,n):
 for bits in product([False,True],repeat=n):
  if all(any(bits[v-1]==sign for v,sign in cl) for cl in clauses):return dict(enumerate(bits,1))
 return None
print("Satisfying assignment:",sat(clauses,5))
