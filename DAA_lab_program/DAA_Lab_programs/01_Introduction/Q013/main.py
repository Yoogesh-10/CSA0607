# DAA Assignment - Question 13
# Topic: Introduction
# Algorithm: Unique paths in grid
# Time complexity: O(mn) time, O(n) space

def unique_paths(m,n):
    dp=[1]*n
    for _ in range(1,m):
        for j in range(1,n):dp[j]+=dp[j-1]
    return dp[-1]
print("Grid 7x3:",unique_paths(7,3))
print("Grid 3x2:",unique_paths(3,2))
