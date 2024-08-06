n=[]
x=int(input("Enter limit of list: "))
for i in range(1, x+1):
    t=int(input("Enter elements: "))
    n.append(t)
n.sort()
p=set(n)
print(f"Second Largest Number is: {list(p)[-2]}")