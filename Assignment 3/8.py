n = int(input("Enter Limit: "))
sum = 0
print("Series:")
for i in range(1, n + 1):
    term = (i ** 2) // i
    sum += term
    print(f"{i}^2/{i}", end=" + " if i < n else "\n")
print(f"Sum of the series: {sum}")