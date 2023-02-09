import os, shutil


#folder = input('Provide folder: ')
prefix = input('Provide prefix: ')
filenames = []

for filename in os.listdir(os.curdir):
    if filename.endswith('.txt'):
        filenames.append(filename)
print('List of files in the folder: ' + str(filenames))

for filename in filenames:
    new_filename = prefix + '_' + filename
    if filename == new_filename or filename.startswith('capitals'):
        continue
    else:
        shutil.move((os.curdir + '/' + filename), (os.curdir + '/' + new_filename))
        print('File ' + filename + ' renamed to file ' + new_filename)