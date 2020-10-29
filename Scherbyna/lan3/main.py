from factory import ProductFactory,CappuccinoFactory,BlackCoffeFactory,LemonadeFactory,HotMilkFactory,CocaColaFactory
from customization import Customization
from preparation import Preparations


factory_product = ProductFactory()
factory_cappuccino = CappuccinoFactory()
factory_black_coffe = BlackCoffeFactory()
factory_lemonade = LemonadeFactory()
factory_hot_milk = HotMilkFactory()
factory_cocacola = CocaColaFactory()

cust = Customization()

cappuccino = factory_cappuccino.get_product()
cappuccino()
"""
float(input(milk- ))
cust.extra_milk
"""