"""
Insertion Sort:
Consider the array split as sorted and unsorted array, take the first in the unsorted array and put it at the correct index of the sorted array.

Time- O(N²)
Space- O(1)

[#5,4,1,3,2]->[#4,#5,1,3,2]->[#1,#4,#5,3,2]->[#1,#3,#4,#5,2]->[#1,#2,#3,#4,#5]

https://www.hackerearth.com/practice/algorithms/sorting/insertion-sort/tutorial/
"""


def insertion_sort(arr):
  for i in range(1, len(arr)):
    temp = arr[i]
    j = i - 1
    while arr[j] > temp and j >= 0:
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = temp
  return arr
