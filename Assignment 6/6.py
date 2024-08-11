lists = [("a", 3), ("b", 1), ("c", 2)]
order = [2, 3, 1]
dict = {key: value for value, key in enumerate(lists)}
list = sorted(lists, key=lambda x: dict[x[1]])
print("Ordered Tuples using external List:")
print(list)