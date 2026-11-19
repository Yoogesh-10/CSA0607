# DAA Assignment - Question 20
# Topic: Brute Force
# Algorithm: String permutations
# Time complexity: O(n·n!)

from itertools import permutations
s="ABC"
print("Permutations:",[''.join(p) for p in permutations(s)])
