
class EventSpace():

    def __init__(self, name):
        self.name = name

    def on_land(self, player):
        print(self.name + "!")
        if self.name == "Go":
            player.receive_payment(200)
        elif self.name == "Jail":
            pass
        elif self.name == "Free Parking":
            # TODO: logic for free parking to collect taxes if flag set to True?
            pass
        elif self.name == "Go To Jail":
            player.current_space = 10 # jail space
            player.suspended_turns = 3 # wait 3 turns, OR roll double, OR pay $50, OR use get out of jail free card

