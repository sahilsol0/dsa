"""
Problem Statement: You are given an array. The task is to reverse the array and print it.

Example 1:
Input: N = 5, arr[] = {5,4,3,2,1}
Output: {1,2,3,4,5}
Explanation: Since the order of elements gets reversed the first element will occupy the fifth position, the second element occupies the fourth position and so on.
"""


def rev_array(arr):
  # O(N)
  for i in range(int(len(arr) / 2)):
    arr[i], arr[(len(arr) - 1) - i] = arr[(len(arr) - 1) - i], arr[i]
  return arr


def recursive_rev_array(arr, start, end):
  if start < end:
    arr[start], arr[end] = arr[end], arr[start]
    recursive_rev_array(arr, start + 1, end - 1)
  return arr


if __name__ == "__main__":
  while True:
    inp = input("Enter a number ")
    if inp == "":
      break
    print("original array", list(inp))
    print("reversed array", rev_array(list(inp)))
    print("reversed array", recursive_rev_array(list(inp), 0, len(inp) - 1))
