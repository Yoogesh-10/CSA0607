# DAA Assignment - Question 47
# Topic: Dynamic Programming
# Algorithm: Fibonacci memoization
# Time complexity: O(n)

from functools import lru_cache
@lru_cache(None)
def fib(n):return n if n<2 else fib(n-1)+fib(n-2)
print("F(10):",fib(10))
