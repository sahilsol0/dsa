"""
Find the second largest element in an array
"""

import random


def second_largest_in(arr):
  if len(arr) < 2:
    return -1

  max_index = None
  second_max_index = None

  for i in range(len(arr)):  # can also use enumerate(arr) instead of range
    if max_index is None or arr[i] > arr[max_index]:
      second_max_index = max_index
      max_index = i
    elif arr[i] != arr[max_index] and (
      second_max_index is None or arr[i] > arr[second_max_index]
    ):
      second_max_index = i

  if second_max_index is None:
    return -1

  return arr[second_max_index], second_max_index


if __name__ == "__main__":
  while True:
    inp = int(input("Enter size of array: "))
    inp_list = [random.randint(0, 100) for x in range(inp)]
    print("Og:", inp_list)
    print("Result:", second_largest_in(inp_list))
