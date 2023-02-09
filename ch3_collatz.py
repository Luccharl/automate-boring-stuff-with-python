from hashlib import new
from typing import Tuple


def collatz(number):
    if number % 2 == 0:
        newnum = number // 2
    else:
        newnum = 3 * number + 1
    print(newnum)
    return newnum

try: 
    num = int(input('Enter a number: '))
    
    while True:
        if num == 1:
            break
        else:
            seq = collatz(num)
            num = seq
        
except ValueError:
    print('Please enter a valid integer')
    
