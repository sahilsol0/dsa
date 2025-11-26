import random
from bubble import bubble_sort
from selection import selection_sort
from insertion import insertion_sort
from merge import merge_sort
from quick import quick_sort


def test_sort(sort_function, arr):
  GREEN = "\033[92m"
  RED = "\033[91m"
  RESET = "\033[0m"
  original = arr.copy()
  expected = sorted(original)
  result = sort_function(original.copy())

  func_name = sort_function.__name__
  print(f"{func_name.replace('_', ' ').upper()}:")
  print("Original:", arr)
  print("Sorted:", result)
  if result == expected:
    print(GREEN + "Correct ✓" + RESET)
  else:
    print(RED + "Incorrect ✗" + RESET)
  print("-" * 50)

  return result == expected


if __name__ == "__main__":
  while True:
    inp = int(input("Enter list size: "))
    inp_list = [random.randint(0, inp) for _ in range(inp)]
    print("-" * 50)

    test_sort(bubble_sort, inp_list)
    test_sort(selection_sort, inp_list)
    test_sort(insertion_sort, inp_list)
    test_sort(merge_sort, inp_list)
    test_sort(quick_sort, inp_list)