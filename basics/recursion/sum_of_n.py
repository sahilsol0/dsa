"""
Problem statement: Given a number ‘N’, find out the sum of the first N natural numbers.

Example 1:
Input: N=5
Output: 15
Explanation: 1+2+3+4+5=15
"""


def sum_of_n(n):
  if n == 0:
    return n
  return n + sum_of_n(n - 1)


if __name__ == "__main__":
  while True:
    inp = int(input("Enter a number: "))
    print("Sum", sum_of_n(inp))
