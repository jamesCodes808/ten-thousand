from game_logic import GameLogic
import sys

class Game:
    def __init__(self, rounds=0, dice=6, rolled_dice=[],
                 round_flag=False, roll_score=0,
                 bank_score=0):
        self.rounds = rounds
        self.dice = dice
        self.rolled_dice = rolled_dice
        self.round_flag = round_flag
        self.roll_score = roll_score
        self.bank_score = bank_score


    def play(self):
        print('Welcome to Ten Thousand')
        print('(y)es to play or (n)o to decline')
        choice = input("> ")
        if choice.lower() == 'n':
            print("OK. Maybe another time")
        else:
            self.round_flag = False
            self.start_round()


    def start_round(self):
        if self.bank_score >= 10000:
            self.round_flag = False
            self.winner_message()
            return

        if self.round_flag is False:
            self.rounds += 1
            print(f'Starting round {self.rounds}')
            self.round_flag = True

        while self.round_flag is True:
            self.rolled_dice = self.roll_dice()
            print('Enter dice to keep, or (q)uit:')
            choice = input("> ")
            if choice.lower() == 'q':
                print("OK. Maybe another time")
                sys.exit()

            # splits and turns choices into list of integers
            choice_list = choice.split()
            choice_list = list(map(int, str(choice_list[0])))

            valid = self.cheat_checker(choice_list)
            print(valid, 'outside of while loop')
            while valid is not True:
                print('Cheater!!! Or possibly made a typo...')
                print('Enter dice to keep, or (q)uit:')
                choice = input("> ")
                choice_list = choice.split()
                choice_list = list(map(int, str(choice_list[0])))

                valid = True
                valid = self.cheat_checker(choice_list)
                print(valid,'inside while, after cheat checker')

            print('broke out of cheater loop')
        # gets unbanked score and number of dice not in the choice list
            self.calculate_points(choice_list)
            if self.roll_score == 0:
                self.farkle_message()
            else:
                # print(round_result)
                self.end_of_roll_prompt()


    def cheat_checker(self, choices_list):
        print(choices_list, 'choices inside cheat checker')
        print(self.rolled_dice, 'rolled list inside of cheat checker')
        return GameLogic.validate_keepers(self.rolled_dice, choices_list)


    def roll_dice(self):
        print(f'Rolling {self.dice} dice...')

        # get random roll
        self.rolled_dice = list(GameLogic.roll_dice(self.dice))

        # prints rolled result
        print(f"*** {' '.join(str(e) for e in self.rolled_dice)} ***")
        return self.rolled_dice


    def calculate_points(self,chosen_dice):
        self.rolled_dice = [int(i) for i in self.rolled_dice]
        chosen_dice = [int(i) for i in chosen_dice]

        print('chosen dice', chosen_dice)
        print('rolled dice', self.rolled_dice)

        dice_match = []

        for die in chosen_dice:
            if die in self.rolled_dice:
                dice_match.append(die)
                self.rolled_dice.remove(die)

        score = GameLogic.calculate_score(dice_match)
        self.roll_score += score
        self.dice = len(self.rolled_dice)
        print(f'You have {self.roll_score} unbanked points and {len(self.rolled_dice)} dice remaining')

    def end_of_roll_prompt(self):
        print('(r)oll again, (b)ank your points or (q)uit:')
        choice = input('> ')
        if choice == 'r':
            self.start_round()
        elif choice == 'b':
            self.store_score()
            self.round_flag = False
        elif choice == 'q':
            print(f'Thanks for playing. You earned {self.bank_score} points')
            self.round_flag = False



    def store_score(self):
        self.dice = 6
        self.bank_score += self.roll_score
        self.round_flag = False
        print(f'You banked {self.roll_score} points in round {self.rounds}')
        self.roll_score = 0
        print(f'Total score is {self.bank_score} points')
        self.start_round()


    def farkle_message(self):
        self.roll_score = 0
        self.dice = 6
        self.round_flag = False
        print("""
        ****************************************
        **        Zilch!!! Round over         **
        ****************************************
        """)
        self.start_round()


    def winner_message(self):
        print(f'You have just won farkle with {self.bank_score} points')

if __name__ == '__main__':
    new_game = Game()
    new_game.play()
