from walk_behavior import WalkBehavior


class NoWalk(WalkBehavior):
    def walk(self):
        print("я не можу ходити")