n=[]
x=int(input("Enter limit of list: "))
for i in range(1, x+1):
    t=int(input("Enter elements: "))
    n.append(t)
n.sort()
print(f"Greatest number in list {n} is {n[-1]}")