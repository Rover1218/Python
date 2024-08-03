n=int(input("Enter limit to check: "))
for i in range(1, n+1):
    if (i%2==0):
        print(f"{i} It is even")
    else:
        print(f"{i} It is odd")
    i+=1