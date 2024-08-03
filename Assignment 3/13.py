initial = float(input("Enter the initial investment amount: "))
annual = float(input("Enter the annual interest rate (as a percentage): "))
years = int(input("Enter the number of years: "))
annual /= 100
investment = initial
for year in range(1, years + 1):
    investment *= (1 + annual)
    print(f"Year {year}: Investment value = {investment:.2f}")
print(f"\nFinal investment value after {years} years: {investment:.2f}")
