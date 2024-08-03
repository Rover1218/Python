terms = int(input("Enter Limit: "))
a, b, c = 0, 1, 1
sum = a + b + c
for i in range(3, terms):
    term = a + b + c
    a = b
    b = c
    c = term
    sum += term
print(f"Sum of the first {terms} terms in the Tribonacci sequence: {sum}")