import os

def most_files(folder):
    current_most_size = 0
    most_size_folder = None
    for folder_name, subfolders, filenames in os.walk(folder):
        if folder_name == folder:
            continue
        if os.path.getsize(folder_name) > current_most_size:
            current_most_size = os.path.getsize(folder_name)
            most_size_folder = os.path.basename(folder_name)
    
    print(f'''The subfolder '{most_size_folder}' is the folder that uses the most disk space in {folder} with {current_most_size} bytes in size''')
    
most_files(os.getcwd())
    
