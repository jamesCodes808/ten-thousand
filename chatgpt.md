# Prompts sent to ChatGPT and the response.

## Prompt 1
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


## Prompt 2
adjust the gamelogic class code to follow these rules: 
- Single fives are worth 50 points
- Single ones are worth 100 points
- Three of a kind are worth 100 points times the number rolled, except for three ones which are worth 1000 points
- If four, five, or six of a kind are rolled, each additional dice doubles the amount of dice previously rolled. For example, 4 die showing the number 3 would be 600 points and 5 die showing the number 3 would be 1200 points
- This makes the highest possible score in a single roll 8000 for six ones (1000 for three ones, after that player multiplies the roll by two for each additional one in that series of rolling.)
- A straight from 1 to 6 is worth 1500 points. If a player fails to roll a straight, they may make one attempt to complete the straight. If the desired number(s) does not turn up on the next roll, that round is a "crap out" even if there are scoring dice on the table i.e. 1's or 5's.
- Three pairs are worth 1000 points, for instance 2+2, 4+4, 5+5. This rule does not count if you roll a quadruple and a pair e.g. 2+2, 2+2, 6+6 unless stated otherwise (some places have their own house rules).
- Full house (3 of a kind plus 2 of a kind) are worth 1,500

## Answer
Sure, I can help you adjust the GameLogic class to follow these rules. Here's an updated implementation:

```python
class GameLogic:
    
    @staticmethod
    def calculate_score(dice_roll):
        """
        Calculate the score of a dice roll according to the rules of Farkle.
        """
        score = 0
        counts = [0] * 7  # initialize a list of counters for each possible dice value
        for value in dice_roll:
            counts[value] += 1  # increment the counter for the current dice value
        # calculate the score based on the counts of each dice value
        if counts[1] >= 1:
            score += counts[1] * 100  # add points for ones
            if counts[1] >= 3:
                score += 700  # add 700 points for three ones
        if counts[5] >= 1:
            score += counts[5] * 50  # add points for fives
            if counts[5] >= 3:
                score += 350  # add 350 points for three fives
        for i in range(1, 7):
            if counts[i] >= 3:
                if i == 1:
                    score += 1000  # add 1000 points for three ones
                else:
                    score += i * 100  # add points for three of any other value
                if counts[i] >= 4:
                    score *= 2  # double the score for four of a kind
                if counts[i] >= 5:
                    score *= 2  # double the score again for five of a kind
                if counts[i] == 6:
                    score *= 2  # double the score again for six of a kind
        if counts == [0, 1, 1, 1, 1, 1, 1]:
            score += 1500  # add 1500 points for a straight
        if counts == [0, 2, 2, 2, 0, 0, 0]:
            score += 1000  # add 1000 points for three pairs
        if counts == [0, 2, 2, 2, 2, 0, 0]:
            score += 1500  # add 1500 points for a full house
        return score
    
    @staticmethod
    def roll_dice(num_dice):
        """
        Roll a given number of dice and return their values as a tuple.
        """
        import random
        return tuple(random.randint(1, 6) for _ in range(num_dice))


```

## Prompt 3
Project named ten-thousand.
Today is all about tackling the highest risk and/or highest priority features - scoring and dice rolling.
Define a GameLogic class in ten_thousand/game_logic.py file.
Handle calculating score for dice roll
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
    def calculate_score(roll):
        """
        Calculates the score for a given dice roll according to the rules of the game.
        
        Args:
            roll: tuple of integers representing a dice roll
            
        Returns:
            an integer representing the roll's score
        """
        score = 0
        counts = [0] * 7 #initialize counts with 7 elements
        
        for die in roll:
            counts[die] += 1
        
        if counts[1] == len(roll): #all ones
            score += 10000
        else:
            for i in range(1, 7):
                if counts[i] >= 3:
                    score += i * 100 # 3 of a kind score
                    counts[i] -= 3
            
            score += counts[1] * 100 #single 1 score
            score += counts[5] * 50 #single 5 score
        
        return score
    
    @staticmethod
    def roll_dice(num_dice):
        """
        Rolls a given number of dice and returns their values in a tuple.
        
        Args:
            num_dice: an integer between 1 and 6 representing the number of dice to roll
            
        Returns:
            a tuple of random values between 1 and 6 with length equal to num_dice
        """
        return tuple(random.randint(1, 6) for _ in range(num_dice))

```

## Prompt 3.1

Please adjust the code to follow these test :
def test_single_five():
    actual = GameLogic.calculate_score((5,))
    expected = 50
    assert actual == expected
def test_single_one():
    actual = GameLogic.calculate_score((1,))
    expected = 100
    assert actual == expected
def test_two_fives():
    actual = GameLogic.calculate_score((5, 5))
    expected = 100
    assert actual == expected
def test_two_ones():
    actual = GameLogic.calculate_score((1, 1))
    expected = 200
    assert actual == expected
def test_one_and_five():
    actual = GameLogic.calculate_score((1, 5))
    expected = 150
    assert actual == expected
def test_zilch():
    actual = GameLogic.calculate_score((2,))
    expected = 0
    assert actual == expected
def test_three_fives():
    actual = GameLogic.calculate_score((5, 5, 5, 2, 2, 3))
    expected = 500
    assert actual == expected
def test_three_ones():
    actual = GameLogic.calculate_score((1, 1, 1, 2, 3, 4))
    expected = 1000
    assert actual == expected
def test_three_ones_and_a_five():
    actual = GameLogic.calculate_score((1, 1, 1, 5))
    expected = 1050
    assert actual == expected
def test_straight():
    actual = GameLogic.calculate_score((1, 6, 3, 2, 5, 4))
    expected = 1500
    assert actual == expected
def test_three_of_a_kind():
    actual = GameLogic.calculate_score((2, 2, 2))
    expected = 200
    assert actual == expected
def test_four_of_a_kind():
    actual = GameLogic.calculate_score((2, 2, 2, 2))
    expected = 400
    assert actual == expected
def test_five_of_a_kind():
    actual = GameLogic.calculate_score((2, 2, 2, 2, 2))
    expected = 600
    assert actual == expected
def test_six_of_a_kind():
    actual = GameLogic.calculate_score((2, 2, 2, 2, 2, 2))
    expected = 800
    assert actual == expected
def test_six_ones():
    actual = GameLogic.calculate_score((1, 1, 1, 1, 1, 1))
    expected = 4000
    assert actual == expected
@pytest.mark.parametrize(
    "test_input,expected",
    [
        (tuple(), 0),
        ((1,), 100),
        ((1, 1), 200),
        ((1, 1, 1), 1000),
        ((1, 1, 1, 1), 2000),
        ((1, 1, 1, 1, 1), 3000),
        ((1, 1, 1, 1, 1, 1), 4000),
        ((2,), 0),
        ((2, 2), 0),
        ((2, 2, 2), 200),
        ((2, 2, 2, 2), 400),
        ((2, 2, 2, 2, 2), 600),
        ((2, 2, 2, 2, 2, 2), 800),
        ((3,), 0),
        ((3, 3), 0),
        ((3, 3, 3), 300),
        ((3, 3, 3, 3), 600),
        ((3, 3, 3, 3, 3), 900),
        ((3, 3, 3, 3, 3, 3), 1200),
        ((4,), 0),
        ((4, 4), 0),
        ((4, 4, 4), 400),
        ((4, 4, 4, 4), 800),
        ((4, 4, 4, 4, 4), 1200),
        ((4, 4, 4, 4, 4, 4), 1600),
        ((5,), 50),
        ((5, 5), 100),
        ((5, 5, 5), 500),
        ((5, 5, 5, 5), 1000),
        ((5, 5, 5, 5, 5), 1500),
        ((5, 5, 5, 5, 5, 5), 2000),
        ((6,), 0),
        ((6, 6), 0),
        ((6, 6, 6), 600),
        ((6, 6, 6, 6), 1200),
        ((6, 6, 6, 6, 6), 1800),
        ((6, 6, 6, 6, 6, 6), 2400),
        ((1, 2, 3, 4, 5, 6), 1500),
        ((2, 2, 3, 3, 4, 6), 0),
        ((2, 2, 3, 3, 6, 6), 1500),
        ((1, 1, 1, 2, 2, 2), 1200),
    ],
)
def test_all(test_input, expected):
    actual = GameLogic.calculate_score(test_input)
    assert actual == expected

## Answer 

```python
from collections import Counter

class GameLogic:
    @staticmethod
    def calculate_score(dice):
        # Check for empty sequence
        if not dice:
            return 0

        # Check for scoring dice
        counts = Counter(dice)
        score = 0

        # Score ones and fives
        score += 100 * (counts[1] % 3) + 50 * (counts[5] % 3)

        # Score triplets
        for value, count in counts.items():
            if count >= 3:
                score += value * 100
                count -= 3

                # Score remaining ones and fives
                if value == 1:
                    score += count * 100
                elif value == 5:
                    score += count * 50

        # Score four-of-a-kind
        for value, count in counts.items():
            if count >= 4:
                score += value * 100

        # Score five-of-a-kind
        for value, count in counts.items():
            if count == 5:
                score += 2 * value * 100

        # Score six-of-a-kind
        for value, count in counts.items():
            if count == 6:
                score += 3 * value * 100

        # Score straight
        if set(dice) == {1, 2, 3, 4, 5, 6}:
            score = 1500

        return score

```