string = input("Enter String: ")
if len(string) < 3 or len(string) % 2 == 0:
    print("Input string must be odd in length and at least 3 characters long.")
else:
    mid = len(string) // 2
    middle = string[mid - 1: mid + 2]
    print("Middle three characters:", middle)