toppers = ["Alice", "Math", 98],
print("Original Details:")
for topper in toppers:
    print(topper)
toppers[0][1] = "History"
toppers[0][2] = 95
print("\nUpdated Details:")
for topper in toppers:
    print(topper)