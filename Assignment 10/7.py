set1 = {1, 2, 3}
set2 = {4, 5, 6}
set3 = {7, 8, 9}
joined_set = set1.copy()
joined_set.update(set2)
joined_set.update(set3)
print("Joined set:", joined_set)