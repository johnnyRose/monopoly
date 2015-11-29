
class PropertyBase():

    def __init__(self):
        self.mortgaged = False
        self.owner = None

    def mortgage(self):
        self.owner.receive_payment(self.price / 2)
        self.mortgaged = True

    def unmortgage(self):
        self.owner.make_payment((self.price / 2) * 1.1) # 10% interest
        self.mortgaged = False

    def on_land(self, player):
        if self.owner == None:
            # TODO: prompt_to_buy()
            print(str(player.current_space) + ": Would you like to purchase " + self.name + " for $" + str(self.price) + "?")
        elif self.owner is not player and not self.mortgaged:
            player.make_payment(self.get_rent(), self.owner)

