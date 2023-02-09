birthdays = {'Nikko': 'January 01', 'Arman': 'July 21', 'Vaughn': 'November 30'}

while True:
    name = input('Enter a name: (blank to quit) ')
    if name == '':
        break
    
    if name in birthdays:
        print(f'{birthdays[name]} is the birthday of {name}')
    else:
        print(f'I do not have the information about {name}\'s birthday ')
        know_birthday = input(f'Do you know {name}\'s birthday? (Y/N) ').upper()
        
        if know_birthday == 'Y':
            bday = input('What date is it? ')
            birthdays[name] = bday
            print('The birthday database updated')
        elif know_birthday == 'N':
            print('Sorry can\'t help you, BYE!')
            break
