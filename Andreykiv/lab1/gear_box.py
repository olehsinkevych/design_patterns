class GearBox:
    """Docstring"""
    def __init__(self, gearRatio, currentGear):
        self.gearRatio = gearRatio
        self.currentGear = currentGear

    def shift_up(self):
        # Program to print 'The GearBox has shifted up'
        print('The GearBox has shifted up')

    def shiftDown(self):
        # Program to print 'The GearBox has shifted down'
        print('The GearBox has shifted down')

    def __str__(self):
        return 'It is gear box of..'
