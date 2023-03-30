
# Define a class called 'GameLogic'.
class GameLogic:
    # Define a static method called 'calculate_score' which takes a list of integers 'dice' as input.
    @staticmethod
    def calculate_score(dice):
        """
           Calculates the score for a given dice roll according to the rules of the game.

           Args:
               roll: tuple of integers representing a dice roll

           Returns:
               an integer representing the roll's score
       """
        # Initialize a variable 'score' to zero.
        score = 0
        # Create a list called 'counts' with seven elements, all set to zero.
        counts = [0] * 7
        # Loop through each die value in the 'dice' list and update the counts value
        for die in dice:
            counts[die] += 1

        # If there are six ones, add 4000 to the score and return it.
        if counts[1] == 6:
            score += 4000
            return score
        # If there are three ones, add 1000 to the score, subtract three from the count of ones in 'counts'
        elif counts[1] == 3:
            score += 1000
            counts[1] -= 3
        # Add the remaining ones to the score.
        score += counts[1] * 100

        # If counts 5 is greater than or equal to 3,
        if counts[5] >= 3:
            # Add 500 to the score
            score += 500
            # Subtract 3 to the counts of 5 to get remaining 5's
            counts[5] -= 3
        # Add 50 for each remaining count of 5
        score += counts[5] * 50

        # Loop through each possible die value from 1 to 6.
        for i in range(1, 7):
            # If there are exactly three of a die value, add the value multiplied by 100 to the score and return it.
            if counts[i] == 3:
                score += i * 100
                return score
            # If the die value is 2 and there are exactly four, add 400 to the score and return it.
            if i == 2 and counts[i] == 4:
                score += 400
                return score
            # If there are 4 of a kind, multiply that die value to 100 then double it
            if counts[i] == 4:
                score += (i * 100) * 2
                return score
            # If there are 5 of a kind, multiply that die value to 100 then triple it
            if counts[i] == 5:
                score += (i * 100) * 3
                return score
            # If there are 6 of a kind, multiply that die value to 100 then quadruple it
            if counts[i] == 6:
                score += (i * 100) * 4

        # Full House: If there is at least one die of each value, set the score to 1500.
        if all(counts[i] > 0 for i in range(1, 7)):
            score = 1500

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
        # Inside the method, import the 'random' module.
        import random
        # Generate 'num_dice' number of random integers between 1 and 6, and return them as a tuple.
        return tuple(random.randint(1, 6) for _ in range(num_dice))

    @staticmethod
    def validate_keepers(roll, keepers):
        temp_rolled = list(roll)
        valid = True
        for die in keepers:
            if die in temp_rolled:
                temp_rolled.remove(die)
                valid = True
                print(temp_rolled, 'inside of cheat checker for loop')
            else:
                valid = False
        return valid

    @staticmethod
    def get_scorers(roll):
        # 5123
        all_dice_score = GameLogic.calculate_score(roll)
        # 150

        if all_dice_score == 0:
            return tuple()

        scoring_dice = []

        # basically goes through each 'node' like in a linked list but as a tuple
        for i, value in enumerate(roll):
           # value: 5 1 2 3
           # start:end:dont include
            print(roll[:i], 'roll[:i]')
            print(roll[i+1:], 'roll[i+1:]')
            print(value, 'value')
            print(i, 'i')
           # first iteration, () + (1,2,3), 2nd (5) + (2,3)
            temp = roll[:i] + roll[i+1:]
            print(temp, 'temp')
           # first iteration: 100
            temp_2 = GameLogic.calculate_score(temp)
            print(temp_2)
            if temp_2 != all_dice_score:
           # appends value = (1)
                scoring_dice.append(value)
                print(scoring_dice, 'scoring dice')

        return tuple(scoring_dice)

