from collections import Counter
def string(s1, s2):
    count1 = dict(Counter(s1))
    count2 = dict(Counter(s2))
    for char in count1:
        if count1[char] > count2.get(char, 0):
            return "Not Possible"
    return "Possible"
s1 = input("Enter 1st String: ")
s2 = input("Enter 2nd String: ")
print(string(s1, s2))