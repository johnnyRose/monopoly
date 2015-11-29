from dice import Dice
from property_base import PropertyBase

class Utility(PropertyBase):
    def __init__(self, name):
        super(Utility, self).__init__()
        self.name = name
        self.price = 150

    def on_land(self, player):
        super(Utility, self).on_land(player)

    def get_rent(self):
        dice = Dice()
        if len(self.owner.utilities_owned) == 1:
            return dice.roll() * 4
        return dice.roll() * 10

