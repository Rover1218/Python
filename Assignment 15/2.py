import csv
with open('records.csv', 'r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    print("Header:", header)
    print("\nData rows:")
    for row in csv_reader:
        print(row)