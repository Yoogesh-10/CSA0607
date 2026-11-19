# DAA Assignment - Question 45
# Topic: Divide and Conquer
# Algorithm: Strassen small matrix demonstration
# Time complexity: O(n³)

def matmul(A,B):
 return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
print(matmul([[1,2],[3,4]],[[5,6],[7,8]]))
print("Classical multiplication complexity: O(n^3)")
