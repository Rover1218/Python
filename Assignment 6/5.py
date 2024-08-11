tuple = ([3, 1, 2], [9, 7, 8], [5, 4, 6])
lists = tuple(sorted(lst) for lst in tuple)
print("Sorted lists in tuple:")
print(lists)