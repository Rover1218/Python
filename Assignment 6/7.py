list = [(1, 'a', 5), (2, 'b', 6), (3, 'c', 5), (4, 'd', 7)]
k = 2
filter = 5
list = [tup for tup in list if tup[k] == filter]
print(f"Tuples where the {k+1}th element is {filter}:")
print(list)