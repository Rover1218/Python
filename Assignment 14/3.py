def count_word(search_word):
    try:
        count = 0
        with open("Data.txt", "r") as file:
            content = file.read()
            words = content.lower().split()
            count = words.count(search_word.lower())
        return count
    except FileNotFoundError:
        print("Error: Data.txt file not found")
        return -1
    except Exception as e:
        print(f"Error: {str(e)}")
        return -1
if __name__ == "__main__":
    word = input("Enter the word to search: ")
    result = count_word(word)
    if result >= 0:
        print(f"The word '{word}' appears {result} times in the file")