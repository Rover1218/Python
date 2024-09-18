frozen_set = frozenset([10, 20, 30, 40, 50, 60, 70])
list_from_frozenset = list(frozen_set)
sliced_list = list_from_frozenset[2:6]
print("Original frozenset:", frozen_set)
print("List from frozenset:", list_from_frozenset)
print("Sliced list:", sliced_list)