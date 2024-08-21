d = {'a': [1, 2, 3], 'b': [4, 5], 'c': [6, 7, 8, 9]}
count = {k: len(v) for k, v in d.items()}
print(count)