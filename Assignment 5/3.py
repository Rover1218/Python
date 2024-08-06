n=[]
u=[]
x=int(input("Enter limit of list: "))
for i in range(1, x+1):
    t=int(input("Enter elements: "))
    n.append(t)
for i in n:
    if i%2!=0:
        u.append(i)
    else:
        continue
print(u)