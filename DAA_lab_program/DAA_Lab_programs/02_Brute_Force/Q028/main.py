# DAA Assignment - Question 28
# Topic: Brute Force
# Algorithm: Brute-force factorial
# Time complexity: O(n)

def factorial(n):
    ans=1
    for x in range(2,n+1):ans*=x
    return ans
print("5! =",factorial(5))
