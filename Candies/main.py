# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 150 конфет. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

import random

total_candies = 150
max_step = 28
player = input('Привет! как тебя зовут? ')
print(f'Отлично {player}! Начнем игру )')


def whoes_first():
    whoes_first = random.randint(0, 1)
    if whoes_first == 1:
        print(f'{player}, ты ходишь первым!')
        return True
    else:
        print('Пeрвым ходит бот')
        return False

def player_step(candy_amount: int, max_step: int) -> int:
    player_step = int(input('Сколько конфет ты возьмешь? '))
    candy_amount -= player_step
    print(f'Игрок {player} забрал {player_step} конфет. На столе осталось {candy_amount} штук')
    return candy_amount

def bot_step(candy_amount: int, max_step: int) -> int:
    if candy_amount < max_step:
        max_step = candy_amount
    bot_step = random.randint(1, max_step)
    candy_amount -= bot_step
    print(f'Бот взял {bot_step} конфет, осталось {candy_amount}. Твой ход!')
    return candy_amount


def game(candy_amount: int, max_step: int):
    while candy_amount > 0:
        if whoes_first == True:
            candy_amount = player_step(candy_amount, max_step)
            if candy_amount == 0:
                print('Ты выиграл!')
            else:
                candy_amount = bot_step(candy_amount, max_step)
                if candy_amount == 0:
                    print('В этот раз бот победил!')
        else:
            candy_amount = bot_step(candy_amount, max_step)
            if candy_amount == 0:
                print('В этот раз бот победил!')
            else:
                candy_amount = player_step(candy_amount, max_step)
                if candy_amount == 0:
                    print('Ты выиграл!')

whoes_first()
game(total_candies, max_step)