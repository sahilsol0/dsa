"""
Problem statement: Given a number ‘N’, find out its factorial .

Example 1:
Input: N=5
Output: 120
Explanation: 1*2*3*4*5=120
"""


def factorial_of_n(n):
  if n <= 0:
    return 1
  return n * factorial_of_n(n - 1)


if __name__ == "__main__":
  while True:
    inp = int(input("Enter a number: "))
    print("Factorial", factorial_of_n(inp))
