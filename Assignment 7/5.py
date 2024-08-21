keys = []
values = []
n=int(input("Enter limit of 1st list: "))
b=int(input("Enter limit of 2nd list: "))
for i in range(1, n+1):
    k=input("Enter keys: ")
    keys.append(k)
for i in range(1, b+1):
    l=int(input("Enter values: "))
    values.append(l)
result = dict(zip(keys, values))
print(result)