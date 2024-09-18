def is_subset(set1, set2):
    return set1.issubset(set2)
def is_superset(set1, set2):
    return set1.issuperset(set2)
set_a = {1, 2, 3, 4}
set_b = {2, 3}
print(f"Set A: {set_a}")
print(f"Set B: {set_b}")
print("Is Set A a subset of Set B?", is_subset(set_b, set_a))
print("Is Set B a superset of Set A?", is_superset(set_b, set_a))