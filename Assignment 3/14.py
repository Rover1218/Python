import calendar
year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))
cal = calendar.TextCalendar(calendar.SUNDAY)
calendar = cal.formatmonth(year, month)
print(calendar)