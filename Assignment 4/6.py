def digits(number):
    while number >= 10:
        number = sum(int(digit) for digit in str(number))
    return number
number = int(input("Enter a number: "))
result = digits(number)
print("The repetitive sum of digits is:", result)