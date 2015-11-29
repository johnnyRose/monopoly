from chance import Chance
from color_property import ColorProperty
from community_chest import CommunityChest
from event_space import EventSpace
from railroad import Railroad
from tax_space import TaxSpace
from utility import Utility

class Board():
    def __init__(self):
        self.spaces = []
        
        self.spaces.append(EventSpace("Go"))
        self.spaces.append(ColorProperty("Mediterranean Avenue", 60, "brown", 2, 2, 10, 30, 90, 160, 250, 50))
        self.spaces.append(CommunityChest())
        self.spaces.append(ColorProperty("Baltic Avenue", 60, "brown", 2, 4, 20, 60, 180, 320, 450, 50))
        self.spaces.append(TaxSpace("Income Tax", True))
        self.spaces.append(Railroad("Reading Railroad"))
        self.spaces.append(ColorProperty("Oriental Avenue", 100, "light blue", 3, 6, 30, 90, 270, 400, 550, 50))
        self.spaces.append(Chance())
        self.spaces.append(ColorProperty("Vermont Avenue", 100, "light blue", 3, 6, 30, 90, 270, 400, 550, 50))
        self.spaces.append(ColorProperty("Connecticut Avenue", 120, "light blue", 3, 8, 40, 100, 300, 450, 600, 50))

        self.spaces.append(EventSpace("Jail"))
        self.spaces.append(ColorProperty("St. Charles Place", 140, "pink", 3, 10, 50, 150, 450, 625, 750, 100))
        self.spaces.append(Utility("Electric Company"))
        self.spaces.append(ColorProperty("States Avenue", 140, "pink", 3, 10, 50, 150, 450, 625, 750, 100))
        self.spaces.append(ColorProperty("Virginia Avenue", 160, "pink", 3, 12, 60, 180, 500, 700, 900, 100))
        self.spaces.append(Railroad("Pennsylvania Railroad"))
        self.spaces.append(ColorProperty("St. James Place", 180, "orange", 3, 14, 70, 200, 550, 750, 950, 100))
        self.spaces.append(CommunityChest())
        self.spaces.append(ColorProperty("Tennessee Avenue", 180, "orange", 3, 14, 70, 200, 550, 750, 950, 100))
        self.spaces.append(ColorProperty("New York Avenue", 200, "orange", 3, 16, 80, 220, 600, 800, 1000, 100))

        self.spaces.append(EventSpace("Free Parking"))
        self.spaces.append(ColorProperty("Kentucky Avenue", 220, "red", 3, 18, 90, 250, 700, 875, 1050, 150))
        self.spaces.append(Chance())
        self.spaces.append(ColorProperty("Indiana Avenue", 220, "red", 3, 18, 90, 250, 700, 875, 1050, 150))
        self.spaces.append(ColorProperty("Illinois Avenue", 240, "red", 3, 20, 100, 300, 750, 925, 1100, 150))
        self.spaces.append(Railroad("B. & O. Railroad"))
        self.spaces.append(ColorProperty("Atlantic Avenue", 260, "yellow", 3, 22, 110, 330, 800, 975, 1150, 150))
        self.spaces.append(ColorProperty("Ventnor Avenue", 260, "yellow", 3, 22, 110, 330, 800, 975, 1150, 150))
        self.spaces.append(Utility("Water Works"))
        self.spaces.append(ColorProperty("Marvin Gardens", 280, "yellow", 3, 24, 120, 360, 850, 1025, 1200, 150))

        self.spaces.append(EventSpace("Go To Jail"))
        self.spaces.append(ColorProperty("Pacific Avenue", 300, "green", 3, 26, 130, 390, 900, 1100, 1275, 200))
        self.spaces.append(ColorProperty("North Carolina Avenue", 300, "green", 3, 26, 130, 390, 900, 1100, 1275, 200))
        self.spaces.append(CommunityChest())
        self.spaces.append(ColorProperty("Pennsylvania Avenue", 320, "green", 3, 28, 150, 450, 1000, 1200, 1400, 200))
        self.spaces.append(Railroad("Short Line Railroad"))
        self.spaces.append(Chance())
        self.spaces.append(ColorProperty("Park Place", 350, "blue", 2, 35, 175, 500, 1100, 1300, 1500, 200))
        self.spaces.append(TaxSpace("Luxury Tax", False))
        self.spaces.append(ColorProperty("Boardwalk", 400, "blue", 2, 50, 200, 600, 1400, 1700, 2000, 200))

