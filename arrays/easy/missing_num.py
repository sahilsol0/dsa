"""
Problem Statement: Given an integer N and an array of size N-1 containing N-1 numbers between 1 to N. Find the number(between 1 to N), that is not present in the given array..
"""

import random


def missing_num(arr):
  n = len(arr) + 1
  sum = 0
  for i in range(0, n - 1):
    sum += arr[i]
  sum_of_n = n * (n + 1) / 2
  return int(sum_of_n - sum)


def missing_num_w_xor(arr):
  pass


if __name__ == "__main__":
  while True:
    inp = int(input("Enter size of array: "))
    inp_list = [x for x in range(1, inp + 1)]
    del inp_list[random.randint(0, inp)]
    print("Og:", inp_list)
    print("Result:", missing_num(inp_list))
