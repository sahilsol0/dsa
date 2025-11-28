"""
Problem Statement: Given an array of integers arr[] and an integer target.

1st variant: Return YES if there exist two numbers such that their sum is equal to the target. Otherwise, return NO.

2nd variant: Return indices of the two numbers such that their sum is equal to the target. Otherwise, we will return {-1, -1}.
"""

import random


def two_sum(arr, k):
  for i in range(len(arr) - 1):
    for j in range(i + 1, len(arr)):
      if arr[i] + arr[j] == k:
        return i, j
  return -1, -1


def optimal_two_sum(arr, k):
  hash_map = {}

  for i in range(len(arr)):
    complement = k - arr[i]

    if complement in hash_map:
      return hash_map[complement], i

    hash_map[arr[i]] = i
  return -1, -1


if __name__ == "__main__":
  while True:
    inp_list = [random.randint(0, 15) for _ in range(0, random.randint(0, 9))]
    print("Org:", inp_list)
    k = int(input("Enter sum: "))
    print("Res:", two_sum(inp_list, k))
    print("Res:", optimal_two_sum(inp_list, k))

