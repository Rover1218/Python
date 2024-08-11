upper, lower, digits = 0, 0, 0
while (char := input("Enter a character (* to stop): ")) != '*':
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1
    elif char.isdigit():
        digits += 1
print("Uppercase letters:", upper)
print("Lowercase letters:", lower)
print("Digits:", digits)