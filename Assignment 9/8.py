def count_case(s):
    upper_count = 0
    lower_count = 0
    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    
    return upper_count, lower_count
sample_str = "The quick Brown Fox"
upper, lower = count_case(sample_str)
print(f"No. of Upper case characters: {upper}")
print(f"No. of Lower case characters: {lower}")