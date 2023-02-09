while True: #infinite loop
    print('Who are you?')
    name = input()
    if name != 'Charl':
        continue #go back to the start of the loop
    print('Hello Charl! What is the secret key? (Hint: a fish)')
    password = input()
    if password == 'swordfish':
        break   #break out of loop
print('Access Granted')