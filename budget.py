class Category:
    def __init__(self, name, ledger):
        self.name = name
        self.ledger = ledger
        ledger = []


    def deposit(self, amount, description):
        if description == "":
            description = " "
        
        self.ledger.append({"amount" : amount, "description": description})


    def withdraw (self, amount, description):
        for x in self.ledger:
            balance = balance + x[0]
        
        if (balance - amount) > 0:
            self.ledger.append({"amount" : amount * - 1, "description": description})
            return True

        else:
            return False


    def get_balance(self):
        for x in self.ledger:
            balance = balance + x[0]
        
        return balance

    def transfer(self, amount, budget_categ):
        

    
    def check_funds(self, amount):

    






def create_spend_chart(categories):
