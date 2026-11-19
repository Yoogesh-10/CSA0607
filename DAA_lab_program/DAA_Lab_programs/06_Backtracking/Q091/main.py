# DAA Assignment - Question 91
# Topic: Backtracking
# Algorithm: Word search
# Time complexity: O(RC·4^L)

def word_search(b,w):
 R,C=len(b),len(b[0])
 def dfs(r,c,i):
  if i==len(w):return True
  if r<0 or c<0 or r>=R or c>=C or b[r][c]!=w[i]:return False
  ch=b[r][c];b[r][c]="#"
  ok=dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1)
  b[r][c]=ch;return ok
 return any(dfs(r,c,0) for r in range(R) for c in range(C))
print(word_search([["A","B","C"],["D","E","F"]],"ABEF"))
