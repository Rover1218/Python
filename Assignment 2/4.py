n=int(input("Enter 1st Side: "))
y=int(input("Enter 1st Side: "))
z=180-(n+y)
if (n<90 and y<90 and z<90):
    print("It is a acute triangle")
elif (n==90 or y==90 or z==90):
    print("It is a right angled triangle")
else:
    print("It is a obtuse triangle")