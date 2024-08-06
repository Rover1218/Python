n=[]
x=int(input("Enter limit of list: "))
for i in range(1, x+1):
    t=int(input("Enter elements: "))
    n.append(t)
o=int(input("Enter elements to search: "))
for i in range(len(n)):
    if n[i]==o:
        print(f"Element found in index: {i}")
        break
else:
    print("Element not found")