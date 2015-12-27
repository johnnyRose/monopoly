from property_base import PropertyBase

class Railroad(PropertyBase):

    def __init__(self, name):
        super(Railroad, self).__init__()
        self.name = name
        self.price = 200
    
    def on_land(self, player, board):
        super(Railroad, self).on_land(player, board)

    def get_rent(self):
        if len(self.owner.owned_railroads) == 1:
            return 25
        if len(self.owner.owned_railroads) == 2:
            return 50
        if len(self.owner.owned_railroads) == 3:
            return 100
        if len(self.owner.owned_railroads) == 4:
            return 200
        
