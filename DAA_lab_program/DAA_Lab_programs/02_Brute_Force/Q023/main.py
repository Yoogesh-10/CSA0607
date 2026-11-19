# DAA Assignment - Question 23
# Topic: Brute Force
# Algorithm: Matrix multiplication
# Time complexity: O(n³)

def multiply(A,B):
    m,k,n=len(A),len(B),len(B[0])
    C=[[0]*n for _ in range(m)]
    for i in range(m):
      for j in range(n):
       for t in range(k):C[i][j]+=A[i][t]*B[t][j]
    return C
print(multiply([[1,2],[3,4]],[[5,6],[7,8]]))
