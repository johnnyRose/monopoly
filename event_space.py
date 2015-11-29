
class EventSpace():

    def __init__(self, name):
        self.name = name

    def on_land(self, player):
        print(self.name + "!")
        if self.name == "Go":
            player.receive_payment(200)
        elif self.name == "Jail": #just visiting
            pass
        elif self.name == "Free Parking":
            # TODO: logic for free parking to collect taxes if flag set to True?
            pass
        elif self.name == "Go To Jail":
            player.go_to_jail()

