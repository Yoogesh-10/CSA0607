# DAA Assignment - Question 12
# Topic: Introduction
# Algorithm: Game of Life one step
# Time complexity: O(mn)

def life(board):
    m,n=len(board),len(board[0]); out=[[0]*n for _ in range(m)]
    for r in range(m):
      for c in range(n):
        neighbors=sum(board[i][j] for i in range(max(0,r-1),min(m,r+2)) for j in range(max(0,c-1),min(n,c+2)) if (i,j)!=(r,c))
        out[r][c]=1 if neighbors==3 or (board[r][c] and neighbors==2) else 0
    return out
b=[[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
print("Next generation:",life(b))
