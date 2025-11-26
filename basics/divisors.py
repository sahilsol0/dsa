"""
Problem Statement: Given an integer N, return all divisors of N.
A divisor of an integer N is a positive integer that divides N without leaving a remainder. In other words, if N is divisible by another integer without any remainder, then that integer is considered a divisor of N.

Input: N = 36
Output: [1, 2, 3, 4, 6, 9, 12, 18, 36]
Explanation: The divisors of 36 are 1, 2, 3, 4, 6, 9, 12, 18, 36.

Input: N = 12
Output: [1, 2, 3, 4, 6, 12]
Explanation: The divisors of 12 are 1, 2, 3, 4, 6, 12.
"""

import math


def divisors(n):
  """
  time- O(N)
  space- O(N)
  """
  all_divisors = []
  for i in range(1, n + 1):
    if n % i == 0:
      all_divisors.append(i)
  return all_divisors


def optimal_divisors(n):
  """
  time- O(sqrt(N))
  space- O(2*sqrt(N))
  """
  all_divisors = []
  for i in range(1, int(math.isqrt(n)) + 1):
    if n % i == 0:
      all_divisors.append(i)
      if i != n // i:
        all_divisors.append(n // i)
  return all_divisors


if __name__ == "__main__":
  while True:
    inp = int(input("Enter a number "))
    print("Divisors", divisors(inp))
    print("Divisors", optimal_divisors(inp))
