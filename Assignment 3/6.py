terms = int(input("Enter Limit: "))
a, b = 0, 1
sum = 0
for i in range(1, terms):
    term = a + b
    a = b
    b = term
    sum += a
print(f"Sum of the first {terms} terms in the Fibonacci sequence: {sum}")