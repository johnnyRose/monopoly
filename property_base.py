
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
        print("Landed on " + self.name + ".")
        if self.owner == None:
            self._prompt_to_buy(player)
        elif self.owner is player:
            print("You already own " + self.name + ".")
        elif not self.mortgaged:
            player.make_payment(self.get_rent(), self.owner)

    def _prompt_to_buy(self, player):
        response = input(str(player.current_space) + ": Would you like to purchase " \
              + self.name + " for $" + str(self.price) + "? (y/n)\n")
        if response == "y":
            player.purchase_property(self)
            print("Purchased " + self.name + " for $" + str(self.price) + ".")
            

