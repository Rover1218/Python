tuple = (1, 2, 3, 2, 4, 5, 3, 6, 7, 5, 8, 1)
items = []
for item in tuple:
    if tuple.count(item) > 1 and item not in items:
        items.append(item)
print("Repeated items in the tuple:", items)