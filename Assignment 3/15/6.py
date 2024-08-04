rows = 5
for i in range(1, rows + 1):
    print(' ' * (rows - i), end='')
    for j in range(1, 2 * i):
        if j % 2 == 1:
            print(1, end='')
        else:
            print(0, end='')
    print()
for i in range(rows - 1, 0, -1):
    print(' ' * (rows - i), end='')
    for j in range(1, 2 * i):
        if j % 2 == 1:
            print(1, end='')
        else:
            print(0, end='')
    print()