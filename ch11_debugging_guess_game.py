import logging
logging.basicConfig(level=logging.DEBUG,
format=' %(asctime)s - %(levelname)s - %(message)s')

import random
guess = ''

logging.debug('Start')
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    toss = random.randint(0, 1) # 0 is tails, 1 is heads
    logging.debug(toss)
    if toss == 0:
        toss = 'tails'
    else:
        toss = 'heads'
        
    if toss == guess: 
        print('You got it!')
        break
    else:
        print('Nope! Guess again!')
        guess = input()
        logging.debug(toss)
        if toss == guess:
            print('You got it!')
            break
        else:
            print('Nope. You are really bad at this game.')
            break

logging.debug('END')