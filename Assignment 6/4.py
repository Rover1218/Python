list = [
    ("a", 2),
    ("b", 3),
    ("c", 2),
    ("d", 4),
    ("e", 3),
    ("f", 5)
]
sorted = sorted(list, key=lambda x: list.count((x[0], x[1])))
print("Sorted list by frequency of the second element:")
print(sorted)    