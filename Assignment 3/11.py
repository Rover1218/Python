x = float(input("Enter the value of x: "))
n = int(input("Enter the number of terms: "))
sum = 0.0
for i in range(1, n + 1):
    term = (1 / i) * ((x - 1) / x) ** i
    sum += term
    print(f"1/{i}*(({x}-1)/{x})^{i}", end=" + " if i < n else "\n")
print("Sum:", sum)