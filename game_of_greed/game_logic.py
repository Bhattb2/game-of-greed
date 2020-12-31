from collections import Counter
import random

class GameLogic:

    def __init__(self, current_round=1):
        self.current_round = current_round

    @staticmethod    
    def roll_dice(dice_available:int) -> int:
        '''
        This function simulates anywhere between 1 and 6 dice rolls.

        Argument: An integer that represents the total number of dice the player is allowed to roll. 

        Output: A tuple of 1-6 values (depending on input) that are between 1 and 6.
        '''
        if dice_available == 0:
            return
        return tuple(random.randint(1, 6) for i in range(dice_available))
    
    @staticmethod
    def calculate_score(roll:tuple) -> int:
        roll_common = Counter(roll).most_common()
        roll_counts = len(roll_common)
        base_points = {1: 1000, 2:100, 3:100, 4:100, 5:100, 6:100}
        single_base_points = {1: 100, 5:50}
        score = 0

        #straight
        if roll_counts == 6:
            return 1500

        #three pairs
        if roll_counts == 3 and roll_common[0][1] == 2 and roll_common[1][1] == 2:
            return 1500

        #score highest count die, remove, repeat
        while roll_common:
            most_common_num = roll_common[0][0]
            most_common_amt = roll_common[0][1]
            
            #three, four, five of a kind
            if most_common_amt >= 3:
                base = most_common_num * base_points[most_common_num]
                extra = most_common_amt - 3
                score += base + (extra * base)

            # single 1s and 5s
            elif most_common_amt < 3 and (most_common_num == 5 or most_common_num == 1):
                score += most_common_amt * single_base_points[most_common_num]

            # remove highest die
            roll_common = roll_common[1:]

        return score
