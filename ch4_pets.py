my_pets = ['Zophie','Pooka', 'Happy']
print('Enter a pet name: ')
name = input()

if name not in my_pets:
    print(f'I do not have a pet name {name}')
else:
    print(f'{name} is my pet')
    