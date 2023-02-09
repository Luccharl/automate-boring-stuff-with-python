def disp_board(board):
    
    #display a 3x3 board
    print()
    print(f'{board[1]} | {board[2]} | {board[3]}' )
    print('--+---+--')
    print(f'{board[4]} | {board[5]} | {board[6]}' )
    print('--+---+--')
    print(f'{board[7]} | {board[8]} | {board[9]}' )
    print()
        
def game():
    
    #tic-tac-toe board associated with numbers 1-9
    tic_tac_toe_board = {1: '1', 2: '2', 3: '3',
                         4: '4', 5: '5', 6: '6',
                         7: '7', 8: '8', 9: '9'}
    
    disp_board(tic_tac_toe_board)
    
    turn = 'X' #first player
     
    #filling the board with X or O
    for _ in range(len(tic_tac_toe_board)):
        
        move = int(input('What is your move? ')) #1-9 input
        tic_tac_toe_board[move] = turn #board[1-9] = [X|O]
        
        disp_board(tic_tac_toe_board)
        
        if tic_tac_toe_board[1] == tic_tac_toe_board[2] == tic_tac_toe_board[3]:
            print(f'{turn} wins!')
            break
        elif tic_tac_toe_board[4] == tic_tac_toe_board[5] == tic_tac_toe_board[6]:
            break
        elif tic_tac_toe_board[7] == tic_tac_toe_board[8] == tic_tac_toe_board[9]:
            break
        elif tic_tac_toe_board[1] == tic_tac_toe_board[4] == tic_tac_toe_board[7]:
            break
        elif tic_tac_toe_board[2] == tic_tac_toe_board[5] == tic_tac_toe_board[8]:
            break
        elif tic_tac_toe_board[3] == tic_tac_toe_board[6] == tic_tac_toe_board[9]:
            break
        elif tic_tac_toe_board[1] == tic_tac_toe_board[5] == tic_tac_toe_board[9]:
            break
        elif tic_tac_toe_board[3] == tic_tac_toe_board[5] == tic_tac_toe_board[7]:
            break
        
        if turn == 'X':
            turn = 'O' #second player
        else:
            turn = 'X'
                
game()