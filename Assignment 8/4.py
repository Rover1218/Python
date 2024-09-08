input_str = input("Enter string: ")
char_count = 0
digit_count = 0
symbol_count = 0
for char in input_str:
    if char.isalpha():    
        char_count += 1
    elif char.isdigit():     
        digit_count += 1
    else:                  
        symbol_count += 1
print("Chars =", char_count)
print("Digits =", digit_count)
print("Symbols =", symbol_count)