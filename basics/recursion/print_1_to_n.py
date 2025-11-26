"""
Problem Description: Given an integer N, write a program to print numbers from 1 to N.
"""


def print_1_to_n(count, n):
  if count > n:
    return
  print(count, end=" ")
  print_1_to_n(count + 1, n)


def backtracked_print_1_to_n(count, n):
  if count > n:
    return
  backtracked_print_1_to_n(count + 1, n)
  print(count, end=" ")


if __name__ == "__main__":
  while True:
    inp = int(input("\nEnter number "))
    print_1_to_n(0, inp)
    backtracked_print_1_to_n(0, inp)
