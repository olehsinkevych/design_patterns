class CarModel:
    def __init__(self, title: str):
        self.title = title


class Engine:
    def __init__(self, capacity: float, number_Of_Cylinders: int):
        self.capacity = capacity
        self.__number_Of_Cylinders = number_Of_Cylinders

    def start(self):
        pass

    def brake(self):
        pass

    def accerate(self):
        pass


class Body:
    def __init__(self, numberOfDoors: int):
        self.number_Of_Doors = numberOfDoors


class Tire:
    def __init__(self, width: float, airPressure: float):
        self.width = width
        self.air_Pressure = airPressure


class Wheel:
    def __init__(self, diameter: float, __tire: Tire):
        self.diameter = diameter

        self.__tire = tire


class Brake:
    def __init__(self, type: str, __wheel: Wheel):
        self.type = type

        self.__wheel = wheel

    def apply(self):
        pass


class Suspension:
    def __init__(self, springRate: float, __wheel: Wheel):
        self.spring_Rate = springRate

        self.__wheel = wheel


class GearBoxType:
    def __init__(self, name: str, remarks: str):
        self.name = name
        self.remarks = remarks


class GearBox:
    def __init__(self, gearRatio: float, currentGear: int, __gear_box_type: GearBoxType):
        self.gear_Ratio = gearRatio
        self.current_Gear = currentGear

        self.__gear_box_type = gear_box_type

    def shiftUp(self):
        pass

    def shiftDown(self):
        pass


class Car:
    def __init__(self, registrationNum: str, year: int, licenseNumber: str, gear_box: GearBox, car_model: CarModel,
                 engine: Engine, body: Body, suspension: Suspension, brake: Brake):
        self.registration_Num = registrationNum
        self.year = year
        self.license_Number = licenseNumber

        self.__gear_box = gear_box
        self.__car_model = car_model
        self.__engine = engine
        self.__body = body
        self.__suspension = suspension
        self.__brake = brake

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


gear_box_type = GearBoxType("name", "remarks")
__gear_box = GearBox(2.2, 2, gear_box_type)

tire = Tire(2, 2.4)
wheel = Wheel(4, tire)
__suspension = Suspension(3, wheel)
__brake = Brake("type", wheel)

__body = Body(4)
__engine = Engine(5, 5)

__car_model = CarModel("model")
myCar = Car("num", 21, "num", __gear_box, __car_model, __engine, __body, __suspension, __brake)
