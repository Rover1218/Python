n=((1, 2 ,3), (4, 5, 6), (7, 8, 9))
print(n)
u=int(input("Enter the element to be searched: "))
for i in n:
  if i[0]==u:
    print(i)
    break
else:
  print("Element not found")