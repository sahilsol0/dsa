"""
Problem Description: Given an integer N, write a program to print numbers from N to 1.
"""


def print_n_to_1(n):
  if n < 0:
    return
  print(n, end=" ")
  print_n_to_1(n - 1)


def backtracked_print_n_to_1(n):
  if n < 0:
    return
  backtracked_print_n_to_1(n - 1)
  print(n, end=" ")


if __name__ == "__main__":
  while True:
    inp = int(input("\nEnter number "))
    print_n_to_1(inp)
    print("\n")
    backtracked_print_n_to_1(inp)
