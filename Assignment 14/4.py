def display_two_char_words():
    try:
        with open("Data.txt", "r") as file:
            for line in file:
                words = line.split()
                for word in words:
                    if len(word.strip()) == 2:
                        print(word)
    except FileNotFoundError:
        print("Error: Data.txt file not found")
display_two_char_words()