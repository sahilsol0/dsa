"""
Selection Sort:
find the minimum in the unsorted array and put it on the front.

Time- O(N²)
Space- O(1)

[5,4,2,3,1]->[1,4,2,3,5]->[1,2,4,3,5]->[1,2,3,4,5]->[1,2,3,4,5]
"""


def selection_sort(arr):
  for i in range(len(arr) - 1):
    smallest = i
    for j in range(i + 1, len(arr)):
      if arr[j] < arr[smallest]:
        smallest = j
    arr[i], arr[smallest] = arr[smallest], arr[i]
  return arr
