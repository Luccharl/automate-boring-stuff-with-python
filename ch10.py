import os

for folder_name, subfolders, files in os.walk('C:\\Users\\Luc\\py'):
    print(f'The current folder is {folder_name}')
    
    for subfolder in subfolders:
        print(f'It\'s subfolder is {subfolder}')
        
    for file_name in files:
        print(f'The files inside it is {file_name}')
        
    print()

