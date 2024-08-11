tuple = ((1, 'apple', 10), (2, 'banana', 20))
def remove(record):
    return record[1] == 'banana'
tuple = tuple(record for record in tuple if not remove(record))
print("Tuple after removing nested records:")
print(tuple)