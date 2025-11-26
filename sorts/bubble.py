"""
Bubble sort:
most naive sort check two consecutive elements and swap if first > second

Time- O(n²)
Space- O()

[5, 4, 3, 2, 1] -> [4,5,3,2,1] -> [4,3,5,2,1] -> [4,3,2,5,1] -> [4,3,2,1,5]

[...4,5]
[...3,4,5]
[...2,3,4,5]
[1, 2, 3, 4, 5]
"""


def bubble_sort(arr):
  for i in range(len(arr)):
    for j in range(len(arr) - 1 - i):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]

  return arr
