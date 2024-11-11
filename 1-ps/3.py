import os

# Replace 'your_directory_path' with the path of the directory you want to list
directory_path = '\python-cwh\Python-cwh'

contents = os.listdir(directory_path)
for item in contents:
        print(item)

