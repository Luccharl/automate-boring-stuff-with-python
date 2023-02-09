import zipfile,os,time

def backup_to_zip(folder):
    print(folder)
    
    num = 1
    while True:
        zip_file_name = f'{os.path.basename(folder)}_{num}.zip'
        print(zip_file_name)
        if not os.path.exists(zip_file_name):
            break
        num += 1
        
    print(f'creating {zip_file_name}...')
    time.sleep(5)
    backup_file = zipfile.ZipFile(zip_file_name, 'w')
    
    for file_names in os.listdir(folder):
        if not file_names.endswith('.py'):
            continue
        backup_file.write(file_names)
    print('Done')
    
backup_to_zip(os.getcwd())
    
