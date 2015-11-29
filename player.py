from color_property import ColorProperty
from railroad import Railroad
from utility import Utility

class Player():

    def __init__(self):
        self.cash = 1500
        self.suspended_turns = 0
        self.current_space = 0
        self.owned_color_properties = []
        self.owned_utilities = []
        self.owned_railroads = []
        self.get_out_of_jail_free_cards = 0

    def move(self, dice):
        number = dice.roll();

        if self.current_space + number > 39:
            print("Passing Go! Collect $200!")
            self.receive_payment(200) # pass go

        self.current_space = (self.current_space + number) % 40

    def make_payment(self, amount, other_player=None):
        self.cash -= amount
        if other_player != None:
            other_player.receive_payment(amount)

    def receive_payment(self, amount):
        self.cash += amount

    def wait_turn(self):
        self.suspended_turns -= 1

    def purchase_property(self, target_property):
        self.make_payment(self.price)
        target_property.owner = self
        
        if isinstance(target_property, ColorProperty):
            self.owned_color_properties.append(target_property)
        elif isinstance(target_property, Railroad):
            self.owned_railroads.append(target_property)
        elif isinstance(target_property, Utility):
            self.owned_utilities.append(target_property)

    

        