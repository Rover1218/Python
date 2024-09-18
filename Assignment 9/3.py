def calculate(x, y):
    sum_value = x + y
    difference = x - y
    product = x * y
    quotient = x / y if y != 0 else None
    return sum_value, difference, product, quotient
x, y = 10, 5
result = calculate(x, y)
sum_value, difference, product, quotient = result
print(f"Sum: {sum_value}")
print(f"Difference: {difference}")
print(f"Product: {product}")
print(f"Quotient: {quotient}")