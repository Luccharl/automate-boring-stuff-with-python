import os, shutil


folder = input('Provide folder: ')
prefix = input('Provide prefix: ')
filenames = []

for filename in os.listdir(folder):
    if filename.startswith(prefix):
        filenames.append(filename)
print('List of files in the folder: ' + str(filenames))


index = 0

for filename in filenames:
    index += 1
    new_filename = prefix + str('%02d' % index) +'.png'
    if filename == new_filename:
        continue
    else:
        shutil.move((folder + filename), (folder + new_filename))
        print('File ' + filename + ' renamed to file ' + new_filename)