import shutil,os,time
from pathlib import Path

p = Path.home()

print('Enter the source path: (folder/folder/file_name))')
current_folder = input()
current_folder = p / current_folder

print()
print('Enter file extension to copy: (.pdf) ')
file_extension = input()

print()
print('''Enter the destination path (folder/folder) or 
create a new folder (folder/new_folder): ''')
new_folder = input()
new_folder = p / new_folder

print()
if not new_folder.exists():
    os.makedirs(new_folder)

if current_folder.exists():
    
    for folder_name, subfolders, file_names in os.walk(current_folder):    
            for file_name in file_names:
                if file_name.endswith(file_extension):
                    folder = os.path.join(folder_name, file_name)
                    print(f'Copying {folder} to {new_folder}...')
                    shutil.copy(folder, new_folder)
                    time.sleep(1)
                else:
                    continue
    print('DONE!')
            
        
else:
    print(f'The path \'{current_folder}\' does not exist: ')


