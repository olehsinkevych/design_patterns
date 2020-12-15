from factory import CappuccinoFactory, BlackCoffeeFactory, LemonadeFactory, HotMilkFactory, CocaColaFactory
from customization import Customization
from preparation import Preparation

while True:
    factory_cappuccino = CappuccinoFactory()
    factory_black_coffee = BlackCoffeeFactory()
    factory_lemon = LemonadeFactory()
    factory_milk = HotMilkFactory()
    factory_coca_cola = CocaColaFactory()

    cust = Customization(float(input("Extra milk - ")), float(input("Sugar - ")), float(input("Mug size - ")))
    cust = (cust.extra_milk, cust.sugar, cust.mug_size)

    prep = Preparation(float(input("Milk - ")), float(input("Water - ")), float(input("Sugar - ")),
                       float(input("Coke - ")), float(input("Coffee - ")), float(input("Flavour - ")),
                       float(input("Tea - ")))
    prep = (prep.milk, prep.water, prep.sugar, prep.coke, prep.liquid_coffee, prep.added_flavour, prep.tea)

    cappuccino = factory_cappuccino.get_product()
    black_coffee = factory_black_coffee.get_product()
    lemon = factory_lemon.get_product()
    milk = factory_milk.get_product()
    coca_cola = factory_coca_cola.get_product()

    cappuccino.make(cappuccino, cust, prep)
    cappuccino.set_milk()
    cappuccino.set_sugar()
    cappuccino.set_coffee()
    print("\n")
    black_coffee.make(black_coffee, cust, prep)
    black_coffee.set_water()
    black_coffee.set_coffee()
    print("\n")
    lemon.make(lemon, cust, prep)
    lemon.set_water()
    lemon.set_sugar()
    lemon.set_lemon_juice()
    print("\n")
    milk.make(milk, cust, prep)
    milk.set_milk(cust[0])
    print("\n")
    coca_cola.make(coca_cola, cust, prep)
    coca_cola.set_water()
    coca_cola.set_coke()