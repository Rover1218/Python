class OverloadExample:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return OverloadExample(self.value + other.value)

    def __mul__(self, other):
        return OverloadExample(self.value * other.value)

    def __str__(self):
        return str(self.value)

a = OverloadExample(10)
b = OverloadExample(20)

result_add = a + b
result_mul = a * b

print(f"Addition: {result_add}")
print(f"Multiplication: {result_mul}")