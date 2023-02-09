import zipfile,os,time

def backup_to_zip(folder):
    folder = os.path.abspath(folder)
    print(folder)
    
    num = 1
    while True:
        zip_file_name = f'{os.path.basename(folder)}_{num}.zip'
        if not os.path.exists(zip_file_name):
            break
        num += 1
        
    print(f'creating {zip_file_name}...')
    time.sleep(5)
    backup_file = zipfile.ZipFile(zip_file_name, 'w')
    #backup_file.write(folder)
    
    for folder_name, subfolders, file_names in os.walk(folder):
        print(f'Adding Files to {folder_name}...')
        backup_file.write(folder_name)
        
        for file_name in file_names:
            new_base = f'{os.path.basename(folder)}_'
            if file_name.startswith(new_base) and file_name.endswith('zip'):
                continue
            backup_file.write(os.path.join(folder_name, file_name))
            
    backup_file.close()
    print('Done')
    
backup_to_zip('DOCX')
    
