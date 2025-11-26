"""
Problem Statement: "Given a string, check if the string is palindrome or not."  A string is said to be palindrome if the reverse of the string is the same as the string.

Example 1:
Input: Str =  “ABCDCBA”
Output: Palindrome
Explanation: String when reversed is the same as string.
"""


def is_palindrome(s):
  if len(s) <= 1:
    return True
  if s[0] != s[-1]:
    return False
  return is_palindrome(s[1:-1])


if __name__ == "__main__":
  while True:
    inp = input("Enter string: ")
    if inp == "":
      break
    print("is palindrome", is_palindrome(inp))
