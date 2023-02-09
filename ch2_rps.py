import random,sys

print('ROCK PAPER SCISSORS (BEST OF 3 WINS GAME)')

wins = 0
lose = 0
ties = 0
    
while True:
    available_moves = ['R','P','S']
    computer_move = random.choice(available_moves)

    print('Enter your move: (R)ock (P)aper (S)cissors or (Q)uit')
    player_move = input().upper()

    if player_move == 'R' or 'P' or 'S':
        if player_move == computer_move:
            print(f'You have chosen {player_move} and The computer has chosen {player_move}')
            print('It is a tie')
            ties += 1
        elif player_move == 'R' and computer_move == 'P':
            print('You have chosen ROCK and The computer has chosen PAPER')
            print('You lose')
            lose += 1
        elif player_move == 'R' and computer_move == 'S':
            print('You have chosen ROCK and The computer has chosen SCISSOR')
            print('You won')
            wins += 1
        elif player_move == 'P' and computer_move == 'R':
            print('You have chosen PAPER and The computer has chosen ROCK')
            print('You won')
            wins += 1
        elif player_move == 'P' and computer_move == 'S':
            print('You have chosen PAPER and The computer has chosen SCISSOR')
            print('You lose')
            lose += 1
        elif player_move == 'S' and computer_move == 'R':
            print('You have chosen SCISSOR and The computer has chosen ROCK')
            print('You lose')
            lose += 1
        elif player_move == 'S' and computer_move == 'P':
            print('You have chosen SCISSOR and The computer has chosen PAPER')
            print('You won')
            wins += 1
        elif player_move == 'Q':
            sys.exit()
        else:
            print('Wrong Input')
        
    print(f'{wins} wins, {lose} losses, {ties} ties')
            
    if wins == 3:
        print('\nYou won the game!')
        break
    elif lose == 3:
        print('\nGame over, you lose!')
        break
   