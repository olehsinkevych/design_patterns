from main import ProductFactory, CappuccinoFactory, Cappuccino,HotMilkFactory, Customization, Preparation


cust = Customization(1, 3, 2)
factory = HotMilkFactory()
cappuccino = factory.get_product(cust)
