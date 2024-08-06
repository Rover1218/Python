n=[]
x=int(input("Enter limit of list: "))
for i in range(1, x+1):
    t=int(input("Enter elements: "))
    n.append(t)
i=sum(n)
print(f"Sum of the list {n} is {i}")