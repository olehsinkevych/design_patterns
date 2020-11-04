from MiniFactory import *
from Parts import *
from Product import *


dd = None
answer = input()
if answer == 'q':
    coffee_parts = CappuccinoFactory.make_preparation(CoffeeParts)
    coffee_maker = CappuccinoFactory.make_coffee()
    coffee_parts.build()
    coffee_maker.assemble(coffee_parts)
elif answer == 'w':
    coffee_parts = BlackCoffeeFactory.make_preparation(CoffeeParts)
    coffee_maker = BlackCoffeeParts.make_coffee()
    coffee_parts.build()
    coffee_maker.assemble(coffee_parts)
elif answer == 'e':
    coffee_parts = HotMilkFactory.make_preparation(CoffeeParts)
    coffee_maker = HotMilkFactory.make_coffee()
    coffee_parts.build()
    coffee_maker.assemble(coffee_parts)
else:
    print("Repeat your order")
