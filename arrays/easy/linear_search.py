"""
O(N)
O(1)
"""

import random


def linear_search(arr, key):
  for i in range(0, len(arr)):
    if arr[i] == key:
      return i
  return -1


if __name__ == "__main__":
  while True:
    inp = int(input("Enter size of array: "))
    inp_list = [random.randint(0, 100) for x in range(inp)]
    print("Og:", inp_list)
    key = int(input("Enter element to search: "))
    print("Result:", linear_search(inp_list, key))
