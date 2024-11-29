class Calculator:
    def __init__(self):
        print("Calculator is ready!")
    
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero is undefined."
        return a / b
if __name__ == "__main__":
    calc = Calculator()
    print("Addition: 5 + 3 =", calc.add(5, 3))
    print("Subtraction: 5 - 3 =", calc.subtract(5, 3))
    print("Multiplication: 5 * 3 =", calc.multiply(5, 3))
    print("Division: 5 / 3 =", calc.divide(5, 3))
    print("Division by zero: 5 / 0 =", calc.divide(5, 0))