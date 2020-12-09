from central_locking import CentralLocking
from gear_locking import GearLocking
from big_wheel import BigWheel

central_locking = CentralLocking("Opel")
gear_locking = GearLocking("BMW")
big_wheel = BigWheel(central_locking, "Suzuki")
big_wheel.assemble()
big_wheel.build_product()

