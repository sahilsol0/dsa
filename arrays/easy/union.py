"""
Problem Statement: Given two sorted arrays, arr1, and arr2 of size n and m. Find the union of two sorted arrays.

The union of two arrays can be defined as the common and distinct elements in the two arrays.

NOTE: Elements in the union should be in ascending order.

O(m+n)
O(m+n)
"""

import random


def union(arr_a, arr_b):
  union = []
  ptr_a, ptr_b = 0, 0
  while ptr_a < len(arr_a) and ptr_b < len(arr_b):
    if arr_a[ptr_a] < arr_b[ptr_b]:
      if not union or union[-1] != arr_a[ptr_a]:
        union.append(arr_a[ptr_a])
        print(union)
      ptr_a += 1
    elif arr_b[ptr_b] < arr_a[ptr_a]:
      if not union or union[-1] != arr_b[ptr_b]:
        union.append(arr_b[ptr_b])
        print(union)
      ptr_b += 1
    else:
      if not union or union[-1] != arr_a[ptr_a]:
        union.append(arr_a[ptr_a])
        print(union)
      ptr_a += 1
      ptr_b += 1

  while ptr_a < len(arr_a):
    if not union or union[-1] != arr_a[ptr_a]:
      union.append(arr_a[ptr_a])
      print(union)
    ptr_a += 1

  while ptr_b < len(arr_b):
    if not union or union[-1] != arr_b[ptr_b]:
      union.append(arr_b[ptr_b])
      print(union)
    ptr_b += 1

  return union


if __name__ == "__main__":
  while True:
    inp = int(input("Enter size of array: "))
    inp_list_a = sorted([random.randint(0, 11) for x in range(inp)])
    inp_list_b = sorted([random.randint(0, 11) for x in range(inp)])
    print("Og:", inp_list_a, "U", inp_list_b)
    print("Result:", union(inp_list_a, inp_list_b))
