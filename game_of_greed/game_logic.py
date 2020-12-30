from collections import Counter

class GameLogic:
    
    @staticmethod
    def calculate_score(roll:tuple) -> int:
        roll = Counter(roll)
        roll_common = roll.most_common()
        roll_counts = len(roll_common)
        most_common_num = roll_common[0][0]
        most_common_amt = roll_common[0][1]
        base_points = {1: 1000, 2:100, 3:100, 4:100, 5:100, 6:100}
        single_base_points = {1: 100, 5:50}

        print("rolled: ", roll, roll_common, roll_counts)

        #straight
        if roll_counts is 6:
            return 1500

        #three, four, five of a kind
        if most_common_amt >= 3:
            base = most_common_num * base_points[most_common_num]
            extra = most_common_amt - 3

            return base + (extra * base)

        # single 1s and 5s
        if most_common_amt < 3 and most_common_num is 5 or most_common_num is 1:
            return most_common_amt * single_base_points[most_common_num]
 
        return 0

        # next step: Track dice. In each return (except straight and 0) pass unscored die back through recursively.