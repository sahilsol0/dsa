"""
Problem Statement: Given an array that contains only 1 and 0 return the count of maximum consecutive ones in the array.
"""

import random


def max_consecutive_ones(arr):
  count = 0
  consecutive_count = 0
  for i, num in enumerate(arr):
    if num == 1:
      count += 1
    else:
      count = 0
    consecutive_count = max(count, consecutive_count)
  return consecutive_count


if __name__ == "__main__":
  while True:
    inp = int(input("Enter size of array: "))
    inp_list = [random.randint(0, 1) for x in range(1, inp + 1)]
    print("Og:", inp_list)
    print("Result:", max_consecutive_ones(inp_list))
