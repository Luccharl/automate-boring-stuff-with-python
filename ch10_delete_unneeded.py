import os

folder = input('Enter path of the folder to search from: ')

for folder_names, subfolders, file_names in os.walk(folder):
    for file_name in file_names:
        folder_path = os.path.join(folder_names, file_name)
        if os.path.getsize(folder_path) > 100000000:
            print(folder_path)
        else:
            continue
                