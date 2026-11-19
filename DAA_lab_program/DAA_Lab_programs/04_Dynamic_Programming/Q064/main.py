# DAA Assignment - Question 64
# Topic: Dynamic Programming
# Algorithm: Decode ways
# Time complexity: O(n)

def decode(s):
 if not s or s[0]=="0":return 0
 dp1=dp2=1
 for i in range(1,len(s)):
  cur=0
  if s[i]!="0":cur+=dp2
  if 10<=int(s[i-1:i+1])<=26:cur+=dp1
  dp1,dp2=dp2,cur
 return dp2
print("Ways:",decode("226"))
