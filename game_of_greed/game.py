from game_logic import GameLogic
from banker import Banker


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

    def start_game(self):
        #increment and start round
        self.round_num += 1
        print(f"Starting round {self.round_num}")

        ## Roll the dice
        print("Rolling 6 dice...")
        roll = self._roller(6)
        formatted_roll = ' '.join(map(str, (roll)))

        print("*** ", formatted_roll, " ***")

        #ask user for values
        user_input = input("Enter dice to keep, or (q)uit:\n> ")

        #keep playing until the user quits
        while user_input != "q":
            break
        
        # if they quit, print quit message
        print("Thanks for playing. You earned 0 points")

if __name__ == "__main__":
    game = Game()
    game.play()