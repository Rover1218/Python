input = input("Enter string: ")
lowercase = ""
uppercase = ""
for char in input:
    if char.islower():
        lowercase += char
    else:
        uppercase += char
output = lowercase + uppercase
print("Output:", output)