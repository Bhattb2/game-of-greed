class Banker:

    def __init__(self, balance=0, shelved=0):
        self.balance = balance 
        self.shelved = shelved
    
    def shelf(self, dice_rolled):
        #store unbanked points
        self.shelved += dice_rolled
        return self.shelved

    def bank(self):
        self.balance += self.shelved
        self.shelved = 0 
        return self.balance

    def clear_shelf(self):
        self.shelved = 0 
        return self.shelved
    