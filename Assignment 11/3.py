import sys
name = input("Enter your name (or type 'exit' to quit): ")
if name.lower() == 'exit':
    print("Exiting the program...")
    sys.exit()
print(f"Hello, {name}! Welcome!")