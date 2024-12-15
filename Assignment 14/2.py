def count_upper_lines():
    try:
        count = 0
        with open("Data.txt", "r") as file:
            for line in file:
                if line.strip():
                    if line[0].isupper():
                        count += 1
        return count
    except FileNotFoundError:
        print("Error: Data.txt file not found")
        return -1
    except Exception as e:
        print(f"Error: {str(e)}")
        return -1
if __name__ == "__main__":
    result = count_upper_lines()
    if result >= 0:
        print(f"Number of lines starting with uppercase: {result}")