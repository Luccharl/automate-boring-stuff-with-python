import sys

while True:
    print('Type exit to exit')
    responses = input()
    if responses == 'exit':
        sys.exit()
    print(f'You typed {responses}')