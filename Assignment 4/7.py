import math
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
gcd = math.gcd(a, b)
lcm = abs(a * b) // gcd
print("GCD:", gcd)
print("LCM:", lcm)