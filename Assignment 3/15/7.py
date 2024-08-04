def print_pattern():
    text = "123454321"
    length = len(text)
    for i in range(length // 2 + 1):
        print(text[:length // 2 - i] + " " * (2 * i) + text[length // 2 + i:])
    for i in range(length // 2 - 1, -1, -1):
        print(text[:length // 2 - i] + " " * (2 * i) + text[length // 2 + i:])
print_pattern()