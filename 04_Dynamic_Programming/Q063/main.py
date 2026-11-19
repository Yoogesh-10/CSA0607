# DAA Assignment - Question 63
# Topic: Dynamic Programming
# Algorithm: Word break
# Time complexity: O(n²)

def word_break(s,words):
 dp=[False]*(len(s)+1);dp[0]=True
 for i in range(1,len(s)+1):
  dp[i]=any(dp[j] and s[j:i] in words for j in range(i))
 return dp[-1]
print(word_break("leetcode",{"leet","code"}))
