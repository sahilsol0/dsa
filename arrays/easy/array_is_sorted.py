"""
Check if the array is sorted i.e. in ascending or descending form
"""

import random


def is_sorted(arr):
  for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
      return False
  return True


if __name__ == "__main__":
  while True:
    inp = int(input("Enter size of array: "))
    inp_list = [random.randint(0, 100) for x in range(inp)]
    if random.randint(0, 2):
      inp_list = sorted(inp_list)
    print("Og:", inp_list)
    print("Result:", is_sorted(inp_list))
