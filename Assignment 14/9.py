def read_file_with_condition(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for i, line in enumerate(lines, 1):
                line = line.strip()
                print(f"Line {i}: {line}")
                if line:
                    print(f"Non-empty line: {line}")
                if 'python' in line.lower():
                    print(f"Line containing 'python': {line}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
    except Exception as e:
        print(f"Error: {str(e)}")
file_path = "sample.txt"
read_file_with_condition(file_path)