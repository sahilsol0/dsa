"""
Problem Statement: Given a non-empty array of integers arr, every element appears twice except for one. Find that single one.

[1,2,3,1,2]
(1^2^3^1^2)
(1^1^2^2^3)
(0^0^3)
(0^3)
(3)
"""

import random


def num_appear_once(arr):
  xor = 0
  for num in arr:
    xor ^= num
  return xor


if __name__ == "__main__":
  while True:
    inp = int(input("Enter size of array: "))
    inp_list = random.sample(range(0, 100), inp)
    inp_list.extend(inp_list)
    single_num = inp_list.pop()
    random.shuffle(inp_list)
    print("Array:", inp_list)
    print("Single:", single_num)
    print("Result:", num_appear_once(inp_list))
