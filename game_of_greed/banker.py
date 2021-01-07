class Banker:

    def __init__(self, balance=0, shelved=0):
        self.balance = balance 
        self.shelved = shelved
    
    def shelf(self, score):
        #store unbanked points
        self.shelved += score
        return self.shelved

    def bank(self):
        self.balance += self.shelved
        self.shelved = 0 
        return self.balance

    def clear_shelf(self):
        self.shelved = 0 
        return self.shelved
    