"""
Problem Statement: Given an integer array nums, find the subarray with the largest sum and return the sum of the elements present in that subarray.
"""
import random

def kadane_sum(arr):
	max_sum=float("-inf")
	current_sum=0

	for num in arr:
		current_sum+=num
		max_sum=max(current_sum, max_sum)
		if current_sum<0:
			current_sum=0
	return max_sum

def kadane_sum_2(arr):
	max_sum=arr[0]
	current_sum=arr[0]
	for num in arr[1:]:
		current_sum=max(num, current_sum+num)
		max_sum=max(max_sum, current_sum)
	return max_sum

if __name__=="__main__":
	while True:
		inp=int(input("enter array size: "))
		inp_list=[random.randint(-1*inp, inp) for _ in range(inp)]
		print("Org:", inp_list)
		print("res", kadane_sum(inp_list))
		print("res -ve", kadane_sum_2(inp_list))
