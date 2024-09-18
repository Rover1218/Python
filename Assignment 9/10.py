def sort_hyphen_separated_words(sequence):
    words = sequence.split('-')
    sorted_words = sorted(words)
    sorted_sequence = '-'.join(sorted_words)
    return sorted_sequence
input_sequence = "green-red-yellow-black-white"
result = sort_hyphen_separated_words(input_sequence)
print(result)