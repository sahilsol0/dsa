"""
Merge Sort:
continuosly split the array and then sort and combine the array.

O(Nlog(N))
"""


def merge(left, right):
  """Merge two sorted lists and return a new sorted list."""
  i = j = 0
  merged = []
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      merged.append(left[i])
      i += 1
    else:
      merged.append(right[j])
      j += 1
  if i < len(left):
    merged.extend(left[i:])
  if j < len(right):
    merged.extend(right[j:])
  return merged


def merge_sort(arr):
  if len(arr) <= 1:
    return arr[:]
  mid = len(arr) // 2
  left_sorted = merge_sort(arr[:mid])
  right_sorted = merge_sort(arr[mid:])
  return merge(left_sorted, right_sorted)
