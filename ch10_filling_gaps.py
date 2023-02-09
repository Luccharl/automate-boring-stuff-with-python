import os,re,shutil
from pathlib import Path

folder = input('Enter folder path: ')
prefix = input('Enter prefix of the file to search: ')

filename_pattern = re.compile(rf'({prefix})(\d*)(.*)')
after_prefix_num = []

for foldernames,subfolders, filenames in os.walk(folder):
    for file_name in filenames:
        match_obj =  filename_pattern.search(file_name)
        if match_obj:
                prefix,number,extension = match_obj.groups()
                
                after_prefix_num.append(number)
        else:
            continue
        
ordered_prefix_num = after_prefix_num.copy()        
      
for item in range(len(ordered_prefix_num)):
    ordered_prefix_num[item] = item
    folder = Path(folder)
    
    old_name = Path(f'{prefix}{after_prefix_num[item]}{extension}')
    new_name = Path(f'{prefix}{ordered_prefix_num[item]}{extension}')
    
    shutil.move(folder / old_name , folder / new_name)

    
