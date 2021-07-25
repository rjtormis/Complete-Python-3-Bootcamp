import random 
def player_first():
        if random.randint(0,1) == 0:
            return 'Player 1'
        else:
            return 'Player 2'

def player_choose():
    choose = ''
    while choose != 'X' or choose != 'O':
        choose=input('Player 1: X or O :').upper()
        if choose == 'X':
            return ('X','O')
        else:
            return ('O','X')

def board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def player_marker(boardlist,marker,position):
    boardlist[position] = marker

def space_checker(board,position):
    return board[position] == ' '

def full_board_checker(board):
    for i in range(1,10):
        if space_checker(board,i):
            return False
    return True

def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) # checking across top
    or (board[4] == mark and board[5] == mark and board[6] == mark) # checking  across middle
    or (board[1] ==mark and board[2] == mark and board[3] == mark) # checking across bottom
    or (board[7] == mark and board[4] == mark and board[1] == mark) # checking down bottom left side
    or (board[8] == mark and board[5] == mark and board[2] == mark) # checking down middle
    or (board[9] == mark and board[6] == mark and board[3] == mark) #checking bottom left side
    or (board[7] == mark and board[5] == mark and board[3] == mark) #checking diagonal
    or (board[1] == mark and board[5] == mark and board[9] == mark)) #checking diagonal

def player_choice(board):
    Position = 0
    while Position not in [1,2,3,4,5,6,7,8,9] or not space_checker(board,Position):
        Position = int(input('Choose your next posistion:'))
    return Position

def replay():
    return input('Do you want to play again? Enter Yes or No:').lower().startswith('y')


def MainGame():
    print('Welcome Players to Tic Tac Toe!')
    while True:
        gameBoard = [' '] * 10
        player1,player2 = player_choose()
        turn = player_first()
        print('\n')
        print(f'Congratulations! {turn} will go first!')
        print('\n')
        play_game = input('Are you ready to play? Yes or No:').lower()
        if play_game[0] == 'y':
            game_on = True
        else:
            game_on = False
        while game_on:
            if turn == 'Player 1':
                board(gameBoard)
                position = player_choice(gameBoard)
                player_marker(gameBoard,player1,position)

                if win_check(gameBoard,player1):
                    board(gameBoard)
                    print("Congratulations Player 1 ! You've won the Game")
                    break
                else:
                    turn = 'Player 2'
            else:
                board(gameBoard)
                position = player_choice(gameBoard)
                player_marker(gameBoard,player2,position)

                if win_check(gameBoard,player2):
                    board(gameBoard)
                    print("Congratulations Player 2 ! You've won the Game")
                    game_on = False
                else:
                    if full_board_checker(gameBoard):
                        board(gameBoard)
                        print('Game is a Draw!')
                        break
                    else:
                        turn = 'Player 1'
        if not replay():
            break

MainGame()
