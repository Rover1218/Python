n = int(input("Enter Limit: "))
sum = 0
term = 1
for i in range(1, n+1):
    sum += term
    print(f"{term}", end=" + " if i < n  else "\n")
    term *= 2
print("Sum:", sum)