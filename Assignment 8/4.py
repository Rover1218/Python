str = input("Enter string: ")
char = 0
digit = 0
symbol = 0
for char in str:
    if char.isalpha():    
        char += 1
    elif char.isdigit():     
        digit += 1
    else:                  
        symbol += 1
print("Chars =", char)
print("Digits =", digit)
print("Symbols =", symbol)