def COUNT():
    try:
        with open("REPEATED.TXT", "r") as file:
            content = file.read()
        word = input("Enter the word to count: ")
        word_count = content.lower().split().count(word.lower())
        print(f"The word '{word}' appears {word_count} times in the file.")
    except FileNotFoundError:
        print("Error: File 'REPEATED.TXT' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    COUNT()