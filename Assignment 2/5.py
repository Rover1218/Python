a=int(input("Enter 1st number: "))
b=int(input("Enter 1st number: "))
c=int(input("Enter 1st number: "))
if (a<b and c<b):
    print(f"{b} is largest")
elif (b<a and c<a):
    print(f"{a} is largest")
else:
    print(f"{c} is largest")