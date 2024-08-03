import math
n = int(input("Enter Limit: "))
sum = 0.0
for i in range(1, n + 1):
    term = i / math.factorial(i)
    sum += term
    print(f"{i}/{i}!", end=" + " if i < n else "\n")
print("Sum:", sum)