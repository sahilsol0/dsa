"""
Sort the array containing three types of elements 0, 1, 2 into three sections.

using Dutch National Flag algorithm

O(n)
"""

import random


def sort(arr):
  left, mid, right = 0, 0, len(arr) - 1

  while mid <= right:
    if arr[mid] == "A":
      arr[left], arr[mid] = arr[mid], arr[left]
      left += 1
      mid += 1
    elif arr[mid] == "B":
      mid += 1
    else:
      arr[mid], arr[right] = arr[right], arr[mid]
      right -= 1
  return arr


if __name__ == "__main__":
  inp = int(input("Enter size: "))
  for _ in range(inp // 4):
    inp_list = [random.choice(["A", "B", "C"]) for _ in range(inp)]
    for item in inp_list:
      print(item, end="")
    print()
    result = sort(inp_list)
    for item in result:
      print(item, end="")
    print()
