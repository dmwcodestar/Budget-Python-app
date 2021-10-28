class budget_class():
    def __init__(self, balance):
        self.balance = balance

    def __repr__(self):
        return f'The remaining balance is {self.balance}'

    def withdraw(self, withdrawal):
        self.balance = self.balance - withdrawal
        return withdrawal

    def deposit(self, deposited):
        self.balance = self.balance + deposited
        return deposited
