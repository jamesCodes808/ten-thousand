from game_logic import GameLogic
# from random import randint

# class Game:
#     def __init__(self, dice, rounds):
#         self.dice = dice
#         self.rounds = rounds
#
#
#     def quitter(self):
#         pass
#


# class Player:
#     def __init__(self, bank, total_score):
#         self.bank = bank
#         self.total_score = total_score

# global rounds
rounds = 0
global dice
dice = 6

def play():
    print('Welcome to Ten Thousand')
    print('(y)es to play or (n)o to decline')
    choice = input("> ")
    if choice.lower() == 'n':
        print("OK. Maybe another time")
    else:
        start_round()
        # start round
        #

def start_round():
    rounds = 0
    rounds += 1
    print(f'Starting round {rounds}')
    print(f'Rolling {dice} dice...')
    rolled_dice = list(GameLogic.roll_dice(dice))
    print(f'*** {rolled_dice} ***')
    print('Enter dice to keep, or (q)uit:')
    choice = input("> ")
    if choice.lower() == 'q':
        print("OK. Maybe another time")
        return
    if choice in rolled_dice:
        print(f'you chose {choice}')
    else:
        start_round()

if __name__ == '__main__':
    # new_game = Game(6, 3)
    play()
