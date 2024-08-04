def print_pattern():
    text = "MADAMADAM"
    length = len(text)
    for i in range(length // 2 + 1):
        print(text[:length // 2 - i] + " " * (2 * i) + text[length // 2 + i:])
    for i in range(length // 2 - 1, -1, -1):
        print(text[:length // 2 - i] + " " * (2 * i) + text[length // 2 + i:])
print_pattern()