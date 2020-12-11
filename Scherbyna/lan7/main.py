from model_raccoon import ModelRaccoon
from wash_dishes_behavior import WashDishesBehavior

mallard.perform_walk()
mallard.perform_scream()

model = ModelRaccoon()
model.perform_walk()
model.set_walk_behavior(WashDishesBehavior())
model.perform_wash()