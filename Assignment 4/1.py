def armstrong(number):
    str = str(number)
    digits = len(str)
    sum = sum(int(digit) ** digits for digit in str)
    return sum == number
number = int(input("Enter a number: "))
if armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")