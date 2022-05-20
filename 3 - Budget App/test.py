import os
import budget

def clear_console():
    """
    PARA LIMPIAR LA PANTALLA DE LA CONSOLA
    """
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

clear_console()
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#

food = budget.Category("Food")
entertainment = budget.Category("Entertainment")
business = budget.Category("Business")
gas = budget.Category("Gas")

# food = budget.Category("Food")
# food.deposit(1000, "initial deposit")
# food.withdraw(10.15, "groceries")
# food.withdraw(15.89, "restaurant and more food for dessert")
# print("food Balance =", food.get_balance())
# clothing = budget.Category("Clothing")
# food.transfer(50, clothing)
# clothing.withdraw(25.55)
# clothing.withdraw(100)
# auto = budget.Category("Auto")
# auto.deposit(1000, "initial deposit")
# auto.withdraw(15)

# print("----------------------------------------------------")
# print(food)
# print(clothing)
# print(auto)
# print("----------------------------------------------------")


# food.deposit(900, "deposit")
# food.deposit(45.56)
# food.deposit(900, "deposit")
# food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
# food.deposit(900, "deposit")
# food.withdraw(45.67)
# food.deposit(900, "deposit")
# food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
# food.deposit(900, "deposit")
# food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
# transfer_amount = 20
# food_balance_before = food.get_balance()
# entertainment_balance_before = entertainment.get_balance()
# good_transfer = food.transfer(transfer_amount, entertainment)
# food_balance_after = food.get_balance()
# entertainment_balance_after = entertainment.get_balance()

# food.deposit(10, "deposit")
# food.deposit(100, "deposit")
# food.withdraw(100.10)

# food.deposit(100, "deposit")
# food.transfer(200, entertainment)

# food.deposit(900, "deposit")
# food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
# food.transfer(20, entertainment)


food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)

# gas.deposit(1500, "deposit")
# gas.withdraw(800, "my car")
# gas.withdraw(200, "my car") 
# gas.withdraw(200, "my car")


# print("----------------------------------------------------")
# print(food)
# print(entertainment)
# print(business)
# # print(gas)
# print("----------------------------------------------------")


# print(create_spend_chart([business,food,entertainment,gas]))

prueba = []
prueba.append(budget.create_spend_chart([business,food,entertainment]))
print(prueba)