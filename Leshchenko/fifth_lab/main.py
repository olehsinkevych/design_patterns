from arrow_shooter_decorator import ArrowShouterDecorator
from crushing_decorator import CrushingDecorator
from character import Character
from stabbing_decorator import StabbingDecorator
from tournament import Tournament


a = CrushingDecorator(ArrowShouterDecorator(Character("Luck")))
b = ArrowShouterDecorator(CrushingDecorator(Character("Max")))
c = StabbingDecorator(ArrowShouterDecorator(Character("Igor")))
tournament = Tournament()
winner_first_part = tournament.start(a, b)
winner = tournament.start(winner_first_part, c)




