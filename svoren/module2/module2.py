import abc

class CoffeeMachine():
    def preparation(self):
        print("Заливаємо воду у кавоварку...")
        print("Засипаємо зерна кави...")
        print("Кладемо стакан у кавоварку...")
    def brewing(self):
        print("Почалось заварення кави...")
        print("Звуки запуску двигуна літака...")
        print("Кава приготована...")
    def milking(self):
        print("Заливаємо молоку у пітчер...")
        print("Включаємо трубку для нагрівання пітчера...")
        print("Молоко заварене...")
    
class Topping(abc.ABC):
    @abc.abstractmethod
    def get_name(self) -> str:
        pass
    @abc.abstractmethod
    def get_price(self) -> float:
        pass

class Milk(Topping):
    def get_name(self):
        return "молоком"
    def get_price(self):
        return 14.0

class Caramel(Topping):
    def get_name(self):
        return "карамеллю"
    def get_price(self):
        return 8.5

class Marshmallow(Topping):
    def get_name(self):
        return "зефіром"
    def get_price(self):
        return 14.0

class Apple(Topping):
    def get_name(self):
        return "яблуком"
    def get_price(self):
        return 9.5

class Menu(CoffeeMachine):
    def menu(self):
        q1 = input("Вітаємо у Joly.Coffee!\nНаша філософія - є лише кава, все решта - доданки.\nБажаєте замовити каву(Y/n):")
        if(q1=='N' or q1=='n'):
            print("Ну то вимітайся.")
            return None
        elif(q1=='Y' or q1=='y'):
            coffee = "Joly.кава"
            price = 30
            q2 = input("Раді чути. Доданки якісь вам здалися?(Y/n):")
            if(q2=='Y' or q2=='y'):
                coffee+=" з "
                q3 = input("Молоко додати?(Y/n):")
                if(q3=='Y' or q3=='y'):
                    milk = Milk()
                    coffee += milk.get_name()
                    price += milk.get_price()
                q4 = input("Карамель?(Y/n):")
                if(q4=='Y' or q4=='y'):
                    if(q3=='Y' or q3=='y'):
                        coffee+= ", "
                    caramel = Caramel()
                    coffee += caramel.get_name()
                    price += caramel.get_price()
                q5 = input("Зефірки, чи як там модно...Маршмелоу?(Y/n):")
                if(q5=='Y' or q5=='y'):
                    if(q3=='Y' or q3=='y' or q4=='Y' or q5=='y'):
                        coffee+= ", "
                    marshmallow = Marshmallow()
                    coffee += marshmallow.get_name()
                    price += marshmallow.get_price()
                q6 = input("У вас є яблоко на телефоні?(Y/n):")
                if(q6=='Y' or q6=='y'):
                    if(q3=='Y' or q3=='y' or q4=='Y' or q5=='y' or q6=='Y' or q6=='y'):
                        coffee+= ", "
                    apple = Apple()
                    coffee += apple.get_name()
                    price += apple.get_price()
            q7 = input("Платити будем?(Y/n):")
            if(q7=='N' or q7=='n'):
                print("Ну то вимітайся.")
                return None
            print("\nВаше замовлення:",coffee,"\nДо оплати",price,"гривень")
            print("Замовлення прийнято.\n")
            self.preparation()
            if(q2!='N' or q2!='n' and q3=='Y' or q3=='y'):
                self.milking()
            self.brewing()
            print("\nОсь ваше замовлення.")
            print('''                         (  ''')
            print('''                           )     (  ''')
            print('''                    ___...(-------)-....___  ''')
            print('''               .-""       )    (          ""-.  ''')
            print('''          .-'``'|-._             )         _.-|  ''')
            print('''         /  .--.|   `""---...........---""`   |  ''')
            print('''        /  /    |                             |  ''')
            print('''        |  |    |                             |  ''')
            print('''         \  \   |                             |  ''')
            print('''          `\ `\ |                             |  ''')
            print('''            `\ `|                             |  ''')
            print('''            _/ /\                             /  ''')
            print('''           (__/  \                           /  ''')
            print('''        _..---""` \                         /`""---.._  ''')
            print('''     .-'           \                       /          '-.  ''')
            print('''    :               `-.__             __.-'              :  ''')
            print('''    :                  ) ""---...---"" (                 :  ''')
            print('''     '._               `"--...___...--"`              _.'  ''')
            print('''       \""--..__                              __..--""/  ''')
            print('''        '._     """----.....______.....----"""     _.'  ''')
            print('''           `""--..,,_____            _____,,..--""`  ''')
            print('''                          `"""----"""` ''')

joly = Menu()
joly.menu()