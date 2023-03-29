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


rounds = 0
global dice
dice = 6
rolled_dice = []

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
    global rounds
    rounds += 1
    print(f'Starting round {rounds}')
    global rolled_dice
    rolled_dice = roll_dice(dice)


    print('Enter dice to keep, or (q)uit:')
    choice = input("> ")

    if choice.lower() == 'q':
        print("OK. Maybe another time")
        return

    # splits and turns choices into list of integers
    choice_list = choice.split()
    choice_list = list(map(int, str(choice_list[0])))

    # gets unbanked score and number of dice not in the choice list
    round_result = calculate_points(choice_list, rolled_dice)
    print(round_result)
    end_of_round_prompt(round_result[0], round_result[1])



def roll_dice(dice):
    print(f'Rolling {dice} dice...')

    # get random roll
    rolled_dice = list(GameLogic.roll_dice(dice))

    # prints rolled result
    print(f"*** {' '.join(str(e) for e in rolled_dice)} ***")
    return rolled_dice

def calculate_points(chosen_dice, rolled_dice):
    rolled_dice = [int(i) for i in rolled_dice]
    chosen_dice = [int(i) for i in chosen_dice]

    print('chosen dice', chosen_dice)
    print('rolled dice', rolled_dice)

    dice_match = []

    for die in chosen_dice:
        if die in rolled_dice:
            dice_match.append(die)
            rolled_dice.remove(die)


    score = GameLogic.calculate_score(dice_match)
    dice = len(rolled_dice)
    print(f'You have {score} unbanked points and {len(rolled_dice)} dice remaining')
    return score, dice



def end_of_round_prompt(score, dice):
    print('(r)oll again, (b)ank your points or (q)uit:')
    choice = input('> ')
    if choice == 'r':
        roll_dice(dice)
        score = calculate_points()
    elif choice == 'b':
        bank_score()
    elif choice == 'q':
        print(f'Thanks for playing. You earned {score} points')

def bank_score():
    pass

if __name__ == '__main__':
    # new_game = Game(6, 3)
    play()


    # roll_dice()
