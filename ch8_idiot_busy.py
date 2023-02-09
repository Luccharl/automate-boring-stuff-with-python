import pyinputplus as pyip

while True:
    response = pyip.inputYesNo('Want to keep an idiot busy? ')
    
    if response == 'no':
        print('Congratulations, you are not an idiot!')
        break
    else: 
        continue