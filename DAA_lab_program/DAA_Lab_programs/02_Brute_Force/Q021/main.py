# DAA Assignment - Question 21
# Topic: Brute Force
# Algorithm: Palindrome substrings
# Time complexity: O(n³)

def pal_substrings(s):
    out=[]
    for i in range(len(s)):
      for j in range(i+1,len(s)+1):
        t=s[i:j]
        if t==t[::-1]:out.append(t)
    return out
print(pal_substrings("aba"))
