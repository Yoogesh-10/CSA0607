# DAA Assignment - Question 26
# Topic: Brute Force
# Algorithm: Rabin-style naive matching demo
# Time complexity: O(nm)

def count_matches(text,pat):
    return sum(text[i:i+len(pat)]==pat for i in range(len(text)-len(pat)+1))
print("Matches:",count_matches("abababa","aba"))
