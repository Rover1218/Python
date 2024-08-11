list = [
    (1, 4, 2),
    (3, 6, 5),
    (7, 8, 9),
    (2, 3, 1)
]
list = sorted(list, key=lambda x: max(x))
print("Sorted tuples by their maximum element:")
print(list)