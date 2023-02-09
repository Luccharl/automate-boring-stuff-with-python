while True:
    age = input('Enter your age: ')
    
    if age.isdecimal():
        break
    print('Please enter a number for your age.')
    
while True:
    password = input('Select a new pasword(letter and numbers only): ')
    if password.isalnum():
        break
    print('Password should only have letters and numbers!')