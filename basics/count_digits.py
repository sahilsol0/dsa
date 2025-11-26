"""
Problem Statement: Given an integer N, return the number of digits in N.
"""

import math


def count_digits(n):
	# # naive approach
	# counter = 0
	# while n > 0:
	#     counter = counter + 1
	#     n = n // 10
	# return counter

	# optimal approach
	return int(math.log10(n) + 1)


if __name__ == "__main__":
	while True:
		a = int(input("Enter a number:"))
		print("No of digits", count_digits(a))
