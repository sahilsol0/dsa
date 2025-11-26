"""
Problem Statement: Palindrome
11211- true
1221- true
12322- false
"""


def is_palindrome(n):
  org = n
  rev = 0
  while n > 0:
    print(n, rev)
    rev = n % 10 + rev * 10
    n = n // 10
  print(n, rev)
  return org == rev


if __name__ == "__main__":
  while True:
    a = int(input("Enter a number:"))
    print("Is palindrome", is_palindrome(a))
