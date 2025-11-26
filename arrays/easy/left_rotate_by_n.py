"""
Problem Statement: Given an integer array nums, rotate the array to the left by n places.

"""

import random


def reverse(arr, low, high):
  while low < high:
    arr[low], arr[high] = arr[high], arr[low]
    low += 1
    high -= 1


def left_rotate_by_k(arr, k):
  n = len(arr)
  if n == 0 or k == 0:
    return arr

  k = k % n

  # reverse first k elements
  reverse(arr, 0, k - 1)

  # reverse the remaining elements
  reverse(arr, k, n - 1)

  # reverse the whole array
  reverse(arr, 0, n - 1)

  # for right rotation
  # - first reverse whole array
  # - then first k elements
  # - at last the remaining elements
  return arr


if __name__ == "__main__":
  while True:
    inp = int(input("Enter size of array: "))
    k = int(input("Enter how much to move: "))
    inp_list = [random.randint(0, inp + 1) for x in range(inp)]
    print("Org:", inp_list)
    result = left_rotate_by_k(inp_list, k)
    print("Res:", result)
