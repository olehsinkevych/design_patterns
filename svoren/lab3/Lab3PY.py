import abc

class Item(abc.ABC):
    @abc.abstractmethod
    def get_name(self) -> str:
        pass
    @abc.abstractmethod
    def get_price(self) -> float:
        pass

class BigMac(Item):
    def get_name(self):
        return "BigMac"
    def get_price(self):
        return 55.5
    
class IceCream(Item):
    def get_name(self):
        return "IceCream"
    def get_price(self):
        return 21.5

class CocaCola(Item):
    def get_name(self):
        return "CocaCola"
    def get_price(self):
        return 24.5

class Tea(Item):
    def get_name(self):
        return "Tea"
    def get_price(self):
        return 18.5

class Meal():
    def __init__(self):
        self.__items = []
    def add_item(self):
        temp1 = int(input("Please enter the position number:"))
        if(temp1==1):
            temp3 = BigMac()
        elif(temp1==2):
            temp3 = IceCream()
        elif(temp1==3):
            temp3 = CocaCola()
        elif(temp1==4):
            temp3 = Tea()
        print(temp3.get_name(),"has been ordered for the amount of",temp3.get_price())
        self.__items.append(temp3)
    def test(self):
        temp = 0
        temp += 1
        print(self.__items[0].get_name(),temp) 
    def get_items(self):
        temp = 0
        total_items = "Your order: "
        for temp in range((len(self.__items))):
            if(temp==0):
                total_items += self.__items[temp].get_name()
            else:
                total_items += ", " + self.__items[temp].get_name()
            temp += 1
        print (total_items)
    def get_price(self):
        temp = 0
        total_price=float(temp)
        for temp in range((len(self.__items))):
            total_price += self.__items[temp].get_price()
            temp += 1
        print ("Your full order price is:",total_price,"UAN")

class MealBuilder():
    def create_menu(self):
        temp=int(input("Welcome to McDonalds. Here's our menu\n1.BigMac 2.IceCream 3.CocaCola 4.Tea\nHow many positions will there be in your order?:"))
        temp2 = Meal()
        for q in range(temp):
            temp2.add_item()
            q += 1
        temp2.get_items()
        temp2.get_price()
    def sell_tea(self):
        temp=int(input("Sorry for the inconvinience but we only have tea available right now.\nHow many cups would you like to order?:"))
        if(temp<0):
            temp=0
        temp2 = Tea()
        if(temp==1):
            print("Your order:",temp,"cup of Tea")
        elif(temp>1):
            print("Your order:",temp,"cups of Tea")
        print("Your full order price is:",temp2.get_price() * temp,"UAN")
        
class BuilderPatternExample():
    def main(self):
        yaroslav = MealBuilder()
        yaroslav.create_menu()
        print("\n")
        yaroslav.sell_tea()

yaroslav2 = BuilderPatternExample()
yaroslav2.main()