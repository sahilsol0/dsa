"""
Problem Statement: Given an integer array sorted in non-decreasing order, remove the duplicates in place such that each unique element appears only once. The relative order of the elements should be kept the same.

If there are k elements after removing the duplicates, then the first k elements of the array should hold the final result. It does not matter what you leave beyond the first k elements.
"""

import random


def remove_duplicates(arr):
  j = 0
  for i in range(1, len(arr)):
    if arr[i] != arr[j]:
      j += 1
      arr[j] = arr[i]
  return arr[: j + 1]


if __name__ == "__main__":
  while True:
    inp = int(input("Enter size of array: "))
    inp_list = sorted([random.randint(0, inp + 1) for x in range(inp)])
    print("Org:", inp_list)
    result = remove_duplicates(inp_list)
    print("Res:", result, list(set(inp_list)) == result)
