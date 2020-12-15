class Screen():
    def screen_on(self):
        print("Дисплей активовано.")
    def screen_off(self):
        print("Дисплей деактивовано.")

class Amplifier():
    def amp_on(self):
        print("Підсилювач активовано.")
    def amp_off(self):
        print("Підсилювач деактивовано.")

class Tuner():
    def tuner_on(self):
        print("Настроювач активовано.")
    def tuner_off(self):
        print("Настроювач деактивовано.")

class DVD_Player():
    def dvd_on(self):
        print("DVD плеєр активовано.")
    def dvd_off(self):
        print("DVD плеєр деактивовано.")

class CD_Player():
    def cd_on(self):
        print("CD плеєр активовано.")
    def cd_off(self):
        print("CD плеєр деактивовано.")

class HomeTheaterFacade():
    def __init__(self,screen:Screen,amp:Amplifier,tuner:Tuner,dvd:DVD_Player,cd:CD_Player):
        self.screen = screen
        self.amp=amp
        self.tuner=tuner
        self.dvd=dvd
        self.cd=cd
        self.dvd2 = 0
        self.cd2 = 0
    def watch_movie(self):
        if(self.dvd2 == 0 and self.cd2 == 0):
            self.screen.screen_on()
            self.amp.amp_on()
            self.tuner.tuner_on()
        choice1=0
        while(choice1!=1 or choice1!=2):
            choice1 = int(input("1.DVD 2.CD\nОберіть плеєр:"))
            if(choice1==1 or choice1==2):
                break
            if(choice1!=1 and choice1!=2):
                print("Ви обрали неправильний номер.")
        choice2=0
        if(choice1==1):
            self.dvd.dvd_on()
            self.dvd2 = 1
            while(choice2!=1 or choice2!=2 or choice2!=3):
                choice2= int(input("1.Одного разу в... Голлівуді 2.Рататуй 3.Гарольд і Кумар відправляються у White Castle\nОберіть ролик:"))
                if(choice2==1 or choice2==2 or choice2==3):
                    break
                if(choice2!=1 and choice2!=2 and choice2!=3):
                    print("Ви обрали неправильний номер.")
        elif(choice1==2):
            self.cd.cd_on()
            self.cd2 = 1
            while(choice2!=1 or choice2!=2 or choice2!=3 or choice2!=4):
                choice2= int(input("1.Radio X 57:45 2.K-DST 1:08:24 3.V Rock 1:18:59 4.Flash FM\nОберіть трек:"))
                if(choice2==1 or choice2==2 or choice2==3 or choice2==4):
                    break
                if(choice2!=1 and choice2!=2 and choice2!=3 or choice2!=4):
                    print("Ви обрали неправильний номер.")
    def stop_movie(self):
        if(self.dvd2 == 0 and self.cd2==0):
            print("Домашній кінотеатр не активовано.")
        else:
            print("Бувайте.")
            if(self.dvd2==1):
                self.dvd.dvd_off
            if(self.cd2==1):
                self.cd.cd_off
            self.tuner.tuner_off()
            self.amp.amp_off()
            self.screen.screen_off()
    
Ted = Screen()
Marshall = Amplifier()
Lily = Tuner()
Barney = DVD_Player()
Robin = CD_Player()

movie_night = HomeTheaterFacade(Ted,Marshall,Lily,Barney,Robin)
breaking_point=0
while(breaking_point!=1):
    choice = int(input("1.Активувати домашній кінотеатр 2.Деактивувати домашній кінотеатр 3.Закінчити сеанс\nОберіть команду:"))
    if(choice==1):
        movie_night.watch_movie()
    elif(choice==2):
        movie_night.stop_movie()
    elif(choice==3):
        breaking_point=1
    else:
        print("Ви обрати неправильний номер.")