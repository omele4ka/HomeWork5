import random

import bot
import view
import 

def start_game():
    whoes_first = random.randint(0, 1)
    if whoes_first == 1:
        main.set_first_turn(True)
    else:
        main.set_first_turn(False)
    while True:
        game()