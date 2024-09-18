def add_elements_to_set(existing_set, elements):
    for element in elements:
        existing_set.add(element)
def display_set(some_set):
    print("The elements in the set are:")
    for element in some_set:
        print(element)
my_set = set()
elements_to_add = ['apple', 'banana', 'cherry', 'apple', 'banana']
add_elements_to_set(my_set, elements_to_add)
display_set(my_set)