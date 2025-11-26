"""
Problem Statement: Given an integer array nums, rotate the array to the left by one.
"""

import random


def left_rotate(arr):
  first_element = arr[0]
  for i in range(len(arr) - 1):
    arr[i] = arr[i + 1]
  arr[-1] = first_element
  return arr


if __name__ == "__main__":
  while True:
    inp = int(input("Enter size of array: "))
    inp_list = sorted([random.randint(0, inp + 1) for x in range(inp)])
    print("Org:", inp_list)
    result = left_rotate(inp_list)
    print("Res:", result)
