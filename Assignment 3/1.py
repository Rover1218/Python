n=int(input("Enter limit: "))
sum=0
for i in range(1, n+1):
    sum+=i
av=sum/n
print(f"{av} is the average of {n} limit")