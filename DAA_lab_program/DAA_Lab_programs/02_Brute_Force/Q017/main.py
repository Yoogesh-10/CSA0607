# DAA Assignment - Question 17
# Topic: Brute Force
# Algorithm: Naive string matching
# Time complexity: O(nm)

def find_pattern(s,p):
    return [i for i in range(len(s)-len(p)+1) if s[i:i+len(p)]==p]
print(find_pattern("AABAACAADAABAABA","AABA"))
