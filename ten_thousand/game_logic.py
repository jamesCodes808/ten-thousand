import random

class GameLogic:
    @staticmethod
    def calculate_score(dice):
        score = 0
        counter = [0] * 7
        for die in dice:
            counter[die] += 1
        if counter[1] > 2:
            score += 1000
            score += (counter[1] - 3) * 100
        else:
            score += counter[1] * 100
        for i in range(2, 7):
            if counter[i] > 2:
                score += i * 100
                if i == 5:
                    score += (counter[i] - 3) * 50
        return score


@staticmethod
def roll_dice(num_dice):
    dice = tuple(random.randint(1, 6) for _ in range(num_dice))
    return dice