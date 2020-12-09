from central_locking import CentralLocking
from gear_locking import GearLocking
from big_wheel import BigWheel

central_locking = CentralLocking("BMW")
gear_locking = GearLocking("Mazda")
big_wheel = BigWheel(central_locking, "SUV")
big_wheel.assemble()
big_wheel.build_product()

