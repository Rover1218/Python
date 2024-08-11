sum, count = 0, 0
negative, cou = 0, 0
while (num := int(input("Enter a number (-1 to stop): "))) != -1:
    if num > 0:
        sum += num
        count += 1
    elif num < 0:
        negative += num
        cou += 1
print("Average of positive numbers:", sum / count if count > 0 else "No positive numbers")
print("Average of negative numbers:", negative / cou if cou > 0 else "No negative numbers")
