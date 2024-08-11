list = [
    ('x', 1),
    ('y', 2),
    ('z', 1)
]
sorted = sorted(list, key=lambda x: (list.count((x[0], x[1]))))
print(sorted)