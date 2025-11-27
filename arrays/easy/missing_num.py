"""
Problem Statement: Given an integer N and an array of size N-1 containing N-1 numbers between 1 to N. Find the number(between 1 to N), that is not present in the given array..
"""

import random


def missing_num(arr, n):
  sum = 0
  for i in range(0, n - 1):
    sum += arr[i]
  sum_of_n = n * (n + 1) // 2
  # or
  # sum_of_n = sum(arr)
  return sum_of_n - sum


def missing_num_w_xor(arr, n):
  """
  Two important properties of XOR:
  - XOR of two same numbers is always 0 i.e. a ^ a = 0.
  - XOR of a number with 0 will result in the number itself i.e. 0 ^ a = a.

  This code works in 3 steps:
  - take xor of all elements in the array(xor_arr)
  - take xor of all numbers from 1 to n(xor_all)
  - take xor of the above two(xor_arr ^ xor_all). This returns the missing number
  """
  xor_arr = 0
  xor_all = 0
  for num in arr:
    xor_arr ^= num
  for i in range(1, n + 1):
    xor_all ^= i

  return xor_arr ^ xor_all


if __name__ == "__main__":
  while True:
    inp = int(input("Enter size of array: "))
    missing = random.randint(1, inp)
    inp_list = [x for x in range(1, inp + 1) if x != missing]
    random.shuffle(inp_list)
    print("Og:", inp_list)
    print("Missing:", missing)
    print("Result:", missing_num(inp_list, inp))
    print("Result:", missing_num_w_xor(inp_list, inp))
