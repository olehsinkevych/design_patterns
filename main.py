class Tire:
    def __init__(self, width, airPressure):
        self._width = width
        self._airPressure = airPressure

    def getwidth(self):
        return self._width

    def getairPressure(self):
        return self._airPressure


class GearBoxType:
    def __init__(self, name, remarks):
        self._name = name
        self._remarks = remarks

    def getname(self):
        return self._name

    def getremarks(self):
        return self._remarks


class Wheel:
    def __init__(self, diameter, tire=Tire):
        self.tire = tire
        self._diameter = diameter

    def getdiameter(self):
        return self._diameter


class Engine:
    def __init__(self, capacity, numberOfCylinders):
        self._capacity = capacity
        self._numberOfCylinders = numberOfCylinders

    def getcapacity(self):
        return self._capacity

    def getnumberOfCylinders(self):
        return self._numberOfCylinders

    def start(self):
        pass

    def brake(self):
        pass

    def accerate(self):
        pass


class GearBox:
    def __init__(self, gearRatio, currentGear, gearboxtype=GearBoxType):
        self.gearboxtype = gearboxtype
        self._gearRatio = gearRatio
        self._currentGear = currentGear

    def getgearRatio(self):
        return self._gearRatio

    def getcurrentGear(self):
        return self._currentGear

    def shiftUp(self):
        pass

    def shiftDown(self):
        pass


class Body:
    def __init__(self, numberOfDoors):
        self._numberOfDoors = numberOfDoors

    def getnumberOfDoors(self):
        return self._numberOfDoors


class Suspension:
    def __init__(self, springRate, wheel=Wheel):
        self.wheel = wheel
        self._springRate = springRate

    def getspringRate(self):
        return self._springRate


class Brake:
    def __init__(self, type, wheel=Wheel):
        self.wheel = wheel
        self._type = type

    def gettype(self):
        return self._type

    def apply(self):
        pass


class Car:
    def __init__(self, registrationNum, year, licenseNumber, engine=Engine, gearbox=GearBox, body=Body,
                 suspension=Suspension, brake=Brake):
        self.engine = engine
        self.gearbox = gearbox
        self.body = body
        self.suspension = suspension
        self.brake = brake
        self._registrationNum = registrationNum
        self._year = year
        self._licenseNumber = licenseNumber

    def getregistr(self):
        return self._registrationNum

    def getyear(self):
        return self._year

    def getlicense(self):
        return self._licenseNumber

    def moveForward(self):
        pass

    def moveBackward(self):
        pass

    def stop(self):
        pass

    def turnRight(self):
        pass

    def turnLeft(self):
        pass


class CarModel:
    def __init__(self, title, car=Car):
        self.car = car
        self._title = title

    def getCar(self):
        return self._title


print("Машина:")
x1 = Tire(12.5, 5.0)
x2 = Wheel(21, x1)
x3 = Suspension(20.5, x2)
x4 = Brake("standart", x2)
x5 = Body(4)
x6 = GearBoxType("name", "remark")
x7 = GearBox(1, 9, x6)
x8 = Engine(2.5, 2)
x9 = Car(1, 2020, "AC7777HA", x8, x7, x5, x3, x4)
x10 = CarModel("LADA", x9)
print("Car Model:", x10.getCar(), "\nregistration number:", x9.getregistr(), "\nyear:", x9.getyear(), "\nlicense number:",
      x9.getlicense(), "\ncapacity:", x8.getcapacity(), "\nnumber of Cylinders:", x8.getnumberOfCylinders(),
      "\nnumber Of Doors:", x5.getnumberOfDoors(), "\ngearRatio:", x7.getgearRatio(), "\ncurrent gear:", x7.getcurrentGear(),
      "\nname of gear box type:", x6.getname(), "\ngear box remarks:", x6.getremarks(), "\nsuspension spring rate",
      x3.getspringRate(), "\nbrake type:", x4.gettype(), "\nwheel diameter:", x2.getdiameter(), "\ntire width:",
      x1.getwidth(), "\ntire air pressure:", x1.getairPressure())