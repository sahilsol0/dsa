"""
Problem Statement: You are given an array of integers, your task is to move all the zeros in the array to the end of the array and move non-negative integers to the front by maintaining their order.
"""

import random


def move_zeroes_to_end(arr):
  """
  This is not so good --> O(n²)
  """
  for i in range(0, len(arr)):
    if arr[i] == 0:
      j = i
      while arr[j] == 0:
        if j == len(arr) - 1:
          return arr
        j += 1
      arr[i], arr[j] = arr[j], arr[i]
  return arr


def optimized_move_zeroes(arr):
  last_non_zero_index = 0
  for i in range(len(arr)):
    if arr[i] != 0:
      arr[last_non_zero_index], arr[i] = arr[i], arr[last_non_zero_index]
      last_non_zero_index += 1
  return arr


if __name__ == "__main__":
  while True:
    inp = int(input("Enter size of array: "))
    inp_list = random.choices(
      population=[0] + list(range(1, 11)), weights=[0.3] + [0.7 / 10] * 10, k=inp
    )
    print("Org:", inp_list)
    # result = move_zeroes_to_end(inp_list)
    result = optimized_move_zeroes(inp_list)
    print("Res:", result)
