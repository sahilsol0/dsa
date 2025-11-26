"""
O(N)
O(1)
"""

import random


def largest_in(arr):
  max_index = 0
  for i in range(1, len(arr)):
    if arr[i] > arr[max_index]:
      max_index = i
  return arr[max_index], max_index


if __name__ == "__main__":
  while True:
    inp = int(input("Enter size of array: "))
    inp_list = [random.randint(0, 100) for x in range(inp)]
    print("Og:", inp_list)
    print("Result:", largest_in(inp_list))
