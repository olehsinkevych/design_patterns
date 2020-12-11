from ingridient import Ingridient
from solt import Solt
from meat import Meat
from bread import Bread
from souse import Souse


burger = ingridient()
ingridient1 = Bread(burger)
ingridient2 = Souse(burger)
ingridient3 = Meat(burger)
ingridient4 = Solt(burger)
print(f'{ingridient1.decorate()}, \n{ingridient2.decorate()}, \n{ingridient3.decorate()}, \n{ingridient4.decorate()}')