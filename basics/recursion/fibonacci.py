"""
Problem Statement: Given an integer N. Print the Fibonacci series up to the Nth term.

1, 1, 2, 3, 5, 8, 13, 21, ...
"""


def fibonacci(n):
  if n <= 0:
    return
  sequence = [0]
  if n >= 2:
    sequence.append(1)
  for i in range(2, n):
    sequence.append(sequence[i - 1] + sequence[i - 2])
  return sequence


def recursive_fibonacci(n):
  if n <= 0:
    return
  if n == 1:
    return [0]
  if n == 2:
    return [0, 1]
  arr = recursive_fibonacci(n - 1)
  arr.append(arr[-1] + arr[-2])
  return arr


if __name__ == "__main__":
  while True:
    inp = int(input("Enter an integer "))
    print("Fibonacci sequence", fibonacci(inp))
    print("Fibonacci sequence", recursive_fibonacci(inp))
