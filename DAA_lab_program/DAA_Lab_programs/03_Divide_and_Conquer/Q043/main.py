# DAA Assignment - Question 43
# Topic: Divide and Conquer
# Algorithm: Recursive palindrome
# Time complexity: O(n)

def pal(s):
 if len(s)<=1:return True
 return s[0]==s[-1] and pal(s[1:-1])
print(pal("racecar"),pal("hello"))
