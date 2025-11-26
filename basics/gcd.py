"""
Problem Statement: Given two integers N1 and N2, find their greatest common divisor.

The Greatest Common Divisor of any two integers is the largest number that divides both integers.
Example 1:
Input:N1 = 9, N2 = 12
Output:3
Explanation:Factors of 9: 1, 3 and 9
Factors of 12: 1, 2, 3, 4, 6, 12
Common Factors: 1, 3 out of which 3 is the greatest hence it is the GCD.

optimal approach uses Euclidian algorithm
gcd(9,12) --> gcd(9, 12-9)
gcd(9,3) --> gcd(9-3, 3)
gcd(6,3) --> gcd(6-3, 3)
gcd(3, 3) --> gcd is 3
better approach is to use modulo instead of subtraction.
gcd(9, 12) --> gcd(9, 12%9)
gcd(9,3) --> gcd(9%3, 3)
gcd(0, 3) --> gcd is 3
"""


def gcd(n1, n2):
  """
  O(min(n1,n2))
  """
  for i in range(min(n1, n2), 0, -1):
    if n1 % i == 0 and n2 % i == 0:
      return i


def euclid_gcd(n1, n2):
  """
  This may look like an improvement but actually is worse than brute force.
  O(max(n1,n2))
  """
  while n1 != n2 and n1 > 0 and n2 > 0:
    old_n1 = n1
    n1 = max(n1, n2) - min(n1, n2)
    n2 = min(n2, old_n1)
  return n1


def optimal_gcd(n1, n2):
  """
  O(log(min(n1, n2)))
  """
  while n2 > 0:
    n1, n2 = n2, n1 % n2
  return n1
  # or
  # while n1 > 0 and n2 > 0:
  #   if n1 > n2:
  #     n1 = n1 % n2
  #   else:
  #     n2 = n2 % n1
  # if n1 == 0:
  #   return n2
  # else:
  #   return n1


if __name__ == "__main__":
  while True:
    n1 = int(input("Enter first number:"))
    n2 = int(input("Enter second number:"))
    print("GCD or HCF:", gcd(n1, n2))
    print("GCD or HCF:", euclid_gcd(n1, n2))
    print("GCD or HCF:", optimal_gcd(n1, n2))
