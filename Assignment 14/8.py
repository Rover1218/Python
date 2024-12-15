with open('data.txt', 'a') as file:
    data = input("Enter data to append: ")
    file.write(data + '\n')