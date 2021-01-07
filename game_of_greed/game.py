from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker


class Game:
    """Class for Game of Greed application
    """

    def __init__(self, num_rounds=20):
        self.banker = Banker()
        self.num_rounds = num_rounds

    def play(self, roller=None):
        """Entry point for playing (or declining) a game
        Args:
            roller (function, optional): Allows passing in a custom dice roller function.
                Defaults to None.
        """
        self.round_num = 0
        self.dice_num = 6
        self._roller = roller or GameLogic.roll_dice

        print("Welcome to Game of Greed")

        print("(y)es to play or (n)o to decline")

        response = input("> ")

        if response == "y" or response == "yes":
            self.start_game()
        else:
            self.decline_game()

    def decline_game(self):
        print("OK. Maybe another time")

    def new_round(self):
        ## Roll the dice
        print("Rolling 6 dice...")
        roll = self._roller(6)
        formatted_roll = ' '.join(map(str, (roll)))

        print("*** ", formatted_roll, " ***")

        #ask user for values
        user_input = input("Enter dice to keep, or (q)uit:\n> ")

        #keep playing until the user quits
        if user_input != "q":
            dice_result = []
            for char in user_input:
                dice_result.append(int(char))   
            score = GameLogic.calculate_score(tuple(dice_result))
            self.banker.shelf(score)
            shelved = self.banker.shelved
            dice_remaining = self.dice_num - len(dice_result)
            print(f"You have {shelved} unbanked points and {dice_remaining} dice remaining")
            bank_decision = input("(r)oll again, (b)ank your points or (q)uit:\n> ")
            if bank_decision == "r" or bank_decision == "roll":
                print("Feature not yet supported.")
                return
            if bank_decision == "b" or bank_decision == "bank":
                self.banker.bank()
                print(f"You banked {score} points in round {self.round_num}")
                print(f"Total score is {self.banker.balance} points")
                return
            if bank_decision == "q" or bank_decision == "quit":
                print(f"Thanks for playing. You earned {self.banker.balance} points")
                exit()      
        
        # if they quit, print quit message
        else: 
            print(f"Thanks for playing. You earned {self.banker.balance} points")
            exit() 

    def start_game(self):
        for i in range(1, self.num_rounds):
            self.round_num += 1
            print(f"Starting round {self.round_num}")
            self.new_round()
        

if __name__ == "__main__":
    game = Game()
    game.play()