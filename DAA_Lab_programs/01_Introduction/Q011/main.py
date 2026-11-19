# DAA Assignment - Question 11
# Topic: Introduction
# Algorithm: Large groups in string
# Time complexity: O(n)

def large_groups(s):
    out=[]; i=0
    while i<len(s):
        j=i
        while j<len(s) and s[j]==s[i]:j+=1
        if j-i>=3:out.append([i,j-1])
        i=j
    return out
s="abbxxxxzzy"
print(s,"->",large_groups(s))
