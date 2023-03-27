# Prompts sent to ChatGPT and the response.

## Prompt
    create a class named gamelogic in python that can Handle calculating score for dice roll
    Add calculate_score static method to GameLogic class.
    The input to calculate_score is a tuple of integers that represent a dice roll.
    The output from calculate_score is an integer representing the roll’s score according to rules of game.
    Handle rolling dice
    Add roll_dice static method to GameLogic class.
    The input to roll_dice is an integer between 1 and 6.
    The output of roll_dice is a tuple with random values between 1 and 6.
    The length of tuple must match the argument given to roll_dice method.
## Answer

    ```python
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
    ```
In this implementation, calculate_score method takes a tuple of integers representing a dice roll and returns an integer representing the score according to the game rules. The rules are as follows:

Each 1 rolled scores 100 points, unless there are three or more, in which case the first three 1s score 1000 points and any additional 1s score 100 points each.

Each 5 rolled scores 50 points, unless there are three or more, in which case the first three 5s score 500 points and any additional 5s score 50 points each.

Any other combination of three of a kind scores 100 times the number on the die (e.g. three 4s score 400 points).

roll_dice method takes an integer between 1 and 6 representing the number of dice to roll, and returns a tuple with random values between 1 and 6. The length of the tuple will be equal to the input integer.