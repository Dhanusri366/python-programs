from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()
options =menu.get_items()
print(options)
coffee = input("enter your coffee")
if(coffee == 'report'):
    coffeeMaker.report()
    moneyMachine.report()
    coffee = input("enter your coffee")

drink =menu.find_drink(coffee)
coffeeMaker.is_resource_sufficient(drink)
if (moneyMachine.make_payment(drink.cost)):

    
    coffeeMaker.make_coffee(drink)

