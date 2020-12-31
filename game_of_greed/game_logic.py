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
 
        


