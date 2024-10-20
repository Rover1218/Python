import os
directory_name = "sample_directory"
if not os.path.exists(directory_name):
    os.mkdir(directory_name)
    print(f"Directory '{directory_name}' created.")
else:
    print(f"Directory '{directory_name}' already exists.")
if os.path.exists(directory_name):
    os.rmdir(directory_name)
    print(f"Directory '{directory_name}' deleted.")