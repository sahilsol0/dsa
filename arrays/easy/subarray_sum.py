"""
Problem Statement: Given an array nums of size n and an integer k, find the length of the longest sub-array that sums to k. If no such sub-array exists, return 0.
"""

import random


def subarray_sum(arr, k):
  lt = 0
  rt = 0
  max_len = 0
  current_sum = arr[0]
  while rt < len(arr):
    while lt <= rt and current_sum > k:
      current_sum -= arr[lt]
      lt += 1
    if current_sum == k:
      max_len = max(max_len, rt - lt + 1)
    rt += 1
    if rt < len(arr):
      current_sum += arr[rt]
  return max_len


if __name__ == "__main__":
  inp_list = [10, 5, 2, 7, 1, 9]
  k = 15
  print("Org:", inp_list, "Sum:", k)
  print("Res:", subarray_sum(inp_list, k))
