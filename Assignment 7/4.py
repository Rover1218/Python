dict = {'a': 1, 'b': 2, 'c': 2, 'd': 3, 'e': 4, 'f': 4}
result = {}
for key, value in dict.items():
    if value not in result.values():
        result[key] = value
print(result)