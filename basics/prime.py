"""
Problem Statement: Given an integer N, check whether it is prime or not. A prime number is a number that is only divisible by 1 and itself and the total number of divisors is 2.
"""

import math


def is_prime(n):
  if n <= 1:
    return False
  for i in range(2, int(math.isqrt(n)) + 1):
    if n % i == 0:
      return False
  return True


if __name__ == "__main__":
  while True:
    inp = int(input("Enter a number "))
    print("Is prime:", is_prime(inp))
