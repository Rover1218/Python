name = input("Enter the full name: ")
parts = name.split()
abbreviation = ""
for part in parts[:-1]:
    abbreviation += part[0].upper() + "."
abbreviation += parts[-1]
print(abbreviation)