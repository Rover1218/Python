def armstrong(number):
    digits = str(number)
    num = len(digits)
    sum1 = sum(int(digit) ** num for digit in digits)
    return sum1 == number
number = int(input("Enter a number: "))
if armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
