from game_logic import GameLogic
import sys

rounds = 0
dice = 6
rolled_dice = []
round_flag = False
roll_score = 0
bank_score = 0


def play():
    global roll_score
    global bank_score
    global rounds
    global round_flag
    print('Welcome to Ten Thousand')
    print('(y)es to play or (n)o to decline')
    choice = input("> ")
    if choice.lower() == 'n':
        print("OK. Maybe another time")
    else:
        round_flag = False
        start_round()



def start_round():
    global rounds
    global round_flag
    global dice
    global rolled_dice
    global roll_score
    global bank_score

    if bank_score >= 10000:
        round_flag = False
        winner_message(bank_score)
        return

    if round_flag is False:
        rounds += 1
        print(f'Starting round {rounds}')
        round_flag = True

    while round_flag is True:
        rolled_dice = roll_dice(dice)
        print('Enter dice to keep, or (q)uit:')
        choice = input("> ")
        if choice.lower() == 'q':
            print("OK. Maybe another time")
            sys.exit()

        # splits and turns choices into list of integers
        choice_list = choice.split()
        choice_list = list(map(int, str(choice_list[0])))

        cheater = cheat_checker(choice_list, rolled_dice)
        print(cheater, 'outside of while loop')
        while cheater:
            print('Cheater!!! Or possibly made a typo...')
            print('Enter dice to keep, or (q)uit:')
            choice = input("> ")
            choice_list = choice.split()
            choice_list = list(map(int, str(choice_list[0])))

            cheater = False
            cheater = cheat_checker(choice_list, rolled_dice)
            print(cheater,'inside while, after cheat checker')

        print('broke out of cheater loop')
    # gets unbanked score and number of dice not in the choice list
        round_result = calculate_points(choice_list, rolled_dice)
        if round_result[0] == 0:
            farkle_message()
        else:
            print(round_result)
            end_of_roll_prompt(round_result[0], round_result[1])

def cheat_checker(choices_list, rolled_list):
    # choice 11 1
    #   2 3 4 5 6
    print(choices_list, 'choices inside cheat checker')
    print(rolled_list, 'rolled list inside of cheat checker')
    temp_rolled = rolled_list[:]
    cheater = False
    for choice in choices_list:
        if choice in temp_rolled:
            temp_rolled.remove(choice)
            print(temp_rolled, 'inside of cheat checker for loop')
        else:
            cheater = True
    return cheater

def roll_dice(dice):
    print(f'Rolling {dice} dice...')

    # get random roll
    rolled_dice = list(GameLogic.roll_dice(dice))

    # prints rolled result
    print(f"*** {' '.join(str(e) for e in rolled_dice)} ***")
    return rolled_dice

def calculate_points(chosen_dice, rolled_dice):
    global dice
    global roll_score
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
    roll_score += score
    dice = len(rolled_dice)
    print(f'You have {roll_score} unbanked points and {len(rolled_dice)} dice remaining')
    return roll_score, dice



def end_of_roll_prompt(score, dice):
    global round_flag
    global rounds
    print('(r)oll again, (b)ank your points or (q)uit:')
    choice = input('> ')
    if choice == 'r':
        start_round()
    elif choice == 'b':
        store_score(score)
        round_flag = False
    elif choice == 'q':
        print(f'Thanks for playing. You earned {score} points')
        round_flag = False



def store_score(score):
    global bank_score
    global rounds
    global dice
    global roll_score
    global round_flag
    dice = 6
    bank_score += score
    roll_score = 0
    round_flag = False
    print(f'You banked {score} points in round {rounds}')
    print(f'Total score is {bank_score} points')
    start_round()

def farkle_message():
    global round_flag
    global dice
    global roll_score
    roll_score = 0
    dice = 6
    round_flag = False
    print("""
    ****************************************
    **        Zilch!!! Round over         **
    ****************************************
    """)
    start_round()

def winner_message(score):
    print(f'You have just won farkle with {score} points')

if __name__ == '__main__':
    # new_game = Game(6, 3)
    play()
    # roll_dice()
