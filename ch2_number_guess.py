import random

print('I am thinking of number between 1 and 20')
num = random.randint(1, 20)
for tries in range(6,0,-1):
    print(f'Take a guess: ({tries} tries left) ')
    guess = int(input())
    
    if guess > num:
        print('Guess is too high')
    elif guess < num:
        print('Guess is too low')
    else:
        break
    
if guess == num:
    print('Good Job! You have correctly guessed what number I was thinking')
else:
    print(f'You ran out of guesses, the number was {num}')
    