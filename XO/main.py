# Создайте программу для игры в ""Крестики-нолики"".
 
import random
 
board = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
 
def get_play_board(board):
    print(f'{board[7]} | {board[8]} | {board[9]}')
    print('-----------')
    print(f'{board[4]} | {board[5]} | {board[6]}')
    print('-----------')
    print(f'{board[1]} | {board[2]} | {board[3]}')
 
def choose_mark():
    player_mark = ' '
    while not (player_mark == 'X' or player_mark == 'O'):
        print('Кем будешь играть, Х или О?')
        player_mark = input().upper()
        if player_mark == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']
 
def whoes_first():
    if random.randint(0, 1) == 0:
        return 'Бот'
    else:
        return 'Ты'
 
def make_move(board, player_mark, move):
    board[move] = player_mark
 
def winner(cell, mark) -> bool:
    return (cell[7] == mark and cell[8] == mark and cell[9] == mark) or (cell[4] == mark and cell[5] == mark and cell[6] == mark) or (cell[1] == mark and cell[2] == mark and cell[3] == mark) or (cell[7] == mark and cell[4] == mark and cell[1] == mark) or (cell[8] == mark and cell[5] == mark and cell[2] == mark) or (cell[9] == mark and cell[6] == mark and cell[3] == mark) or (cell[1] == mark and cell[5] == mark and cell[9] == mark) or (cell[7] == mark and cell[5] == mark and cell[3] == mark)
 
def get_board_copy(board):
    board_copy = []
    for i in board:
        board_copy.append(i)
    return board_copy
 
def is_cell_free(board, move):
    return board[move] == ' '
    
def player_move(board):
    move = '0'

    while move not in '1 2 3 4 5 6 7 8 9' or not is_cell_free(board, int(move)):
        print('Введите номер ячейки ')
        move = input()
    return int(move)
 
def choose_random_move(board, move_list):
    possible_moves = []
    for i in move_list:
        if is_cell_free(board, i):
            possible_moves.append(i)
    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None
 
def bot_move(board, bot_mark):
    if bot_mark == 'X':
        player_mark == 'O'
    else:
        player_mark == 'X'
    for i in range(1, 10):
        board_copy = get_board_copy(board)
        if is_cell_free(board_copy, i):
            make_move(board_copy, bot_mark, i)
            if winner(board_copy, bot_mark):
                return i
    for i in range(1, 10):
        board_copy = get_board_copy(board)
        if is_cell_free(board_copy, i):
            make_move(board_copy, player_mark, i)
            if winner(board_copy, player_mark):
                return i
    move = choose_random_move(board, [1, 3, 7, 9])
    if move != None:
        return move
    if is_cell_free(board, 5):
            return 5
    return choose_random_move(board, [2, 4, 6, 8])
 
def board_full(board):
    for i in range(1, 10):
        if is_cell_free(board, i):
            return False
    return True
 
print('Игра Крестики- Нолики')
 
while True:
    the_board = [' '] * 10
    player_mark, bot_mark = choose_mark()
    turn = whoes_first()
    print(f'{turn} первый!')
    game_playing = True
    while game_playing:
        if turn == 'Ты':
            get_play_board(the_board)
            move = player_move(the_board)
            make_move(the_board, player_mark, move)
 
            if winner(the_board, player_mark):
                get_play_board(the_board)
                print('Ура! Ты победил!')
                game_playing = False
            else:
                if board_full(the_board):
                    get_play_board(the_board)
                    print('Вы сыграли вничью')
                    game_playing = False
                else:
                    turn = 'Бот'
        else:
            move = bot_move(the_board, bot_mark)
            make_move(the_board, bot_mark, move)
 
            if winner(the_board, bot_mark):
                get_play_board(the_board)
                print('Увы! Бот победил')
                game_playing = False
            else:
                if board_full(the_board):
                    get_play_board(the_board)
                    print('Вы сыграли вничью')
                    game_playing = False
                else:
                    turn = 'Ты'