class budget_extended():
    def __init__(self, rent, food, essentials, leisure):
        self.rent = 0
        self.food = 0
        self.essentials = 0
        self.leisure = 0
        self.income = 0
        self.total_expenses_sum = [] #stretch goal add total expenses to a list
    
    def __repr__(self):
        return f'you have a starting balance of {self.rent} {self.food} {self.essentials} {self.leisure} & a starting income of {self.income}'
    
    def add_to_rent(self):
        user_rent = input('How much is your rent?')
        return user_rent
    
    def add_to_food(self):
        user_food = input('How much is your food?')
        return user_food
    
    def add_to_essentials(self):
        user_essentials = input('How much is your essentials?')
        return user_essentials
    
    def add_to_leisure(self):
        user_leisure = input('How much is your leisure?')
        return user_leisure
    
    def add_to_income(self):
        user_income = input('How much is your income?')
        return user_income
    
    def total_expenses(self):
        self.total_expenses_sum = sum({self.rent}, {self.rent},{self.essentials},{self.leisure})
        
    def total_leftover_cash(self):
        self.left_over = ({self.income} - {self.total_expenses})   
        
    def advice_for_user(self):
        if self.total_expenses > self.income:
            return 'you need to either increase your income or reduce your expenses.'
        else:
            return f'you have a budget surplus of {self.left_over}'