import random

class Dice():

    rolled_doubles = False
    
    def roll(self):
        num1 = random.randrange(1, 7)
        num2 = random.randrange(1, 7)
        print("\n\nRolled " + str(num1) + " and " + str(num2) + "!")
        self.rolled_doubles = num1 == num2
        return num1 + num2
    
