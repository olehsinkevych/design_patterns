from abc import ABC, abstractmethod

class Item(ABC):
    abstractmethod
    def get_name(self) -> str:
        pass
    abstractmethod
    def get_price(self) -> float:
        pass

class BigMac(Item):
    def get_name(self):
        return "БігМак"
    def get_price(self):
        return 59.5
    
class IceCream(Item):
    def get_name(self):
        return "Морозиво"
    def get_price(self):
        return 14.5

class CocaCola(Item):
    def get_name(self):
        return "Кока-Кола"
    def get_price(self):
        return 28.5

class Tea(Item):
    def get_name(self):
        return "Чай"
    def get_price(self):
        return 17.5

class Meal():
    def __init__(self):
        self.__items = []
    def add_item(self):
        temp1 = int(input("Будь-ласка введіть номер позиції:"))
        if(temp1==1):
            temp3 = BigMac()
        elif(temp1==2):
            temp3 = IceCream()
        elif(temp1==3):
            temp3 = CocaCola()
        elif(temp1==4):
            temp3 = Tea()
        print(temp3.get_name(),"було замовлено за",temp3.get_price(), "гривень")
        self.__items.append(temp3)
    def test(self):
        temp = 0
        temp += 1
        print(self.__items[0].get_name(),temp) 
    def get_items(self):
        temp = 0
        total_items = "Ваше замовлення: "
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
        print ("До оплати:",total_price,"гривень")

class MealBuilder():
    def create_menu(self):
        temp=int(input("Вітаємо у МакДональдз, ось наше меню:\n1.БігМак 2.Морозиво 3.Кока-кола 4.Чай\nСкільки позицій буде у вашому замовленні?:"))
        temp2 = Meal()
        for q in range(temp):
            temp2.add_item()
            q += 1
        temp2.get_items()
        temp2.get_price()
    def sell_tea(self):
        temp=int(input("Приносимо вибачення за незручності, на данний момент можемо вам запропонувати тільки чай.\nСкільки стаканів чаю ви би хотіли замовити?:"))
        if(temp<0):
            temp=0
        temp2 = Tea()
        if(temp==1):
            print("Ваше замовлення:",temp,"стакан чаю")
        elif(temp>1):
            print("Ваше замовлення:",temp,"стаканів чаю")
        print("До оплати:",temp2.get_price() * temp,"гривень")
        
class BuilderPatternExample():
    def main(self):
        banan = MealBuilder()
        banan.create_menu()
        print("\n")
        banan.sell_tea()

stormtrooper = BuilderPatternExample()
stormtrooper.main()