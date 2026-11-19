# DAA Assignment - Question 1
# Topic: Introduction
# Algorithm: Palindrome check
# Time complexity: O(n·k)

def first_palindrome(words):
    for word in words:
        if word == word[::-1]: return word
    return ""
words=["abc","car","ada","racecar","cool"]
print("Input:", words)
print("First palindrome:", first_palindrome(words))
