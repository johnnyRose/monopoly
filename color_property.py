from property_base import PropertyBase

class ColorProperty(PropertyBase):

    def __init__(self, name, price, color, group_quantity, rent, rent_1h, rent_2h, rent_3h, rent_4h, rent_hotel, house_price):
        super(ColorProperty, self).__init__()

        self.name = name
        self.price = price
        self.color = color
        self.group_quantity = group_quantity
        self.rent = rent
        self.rent_1h = rent_1h
        self.rent_2h = rent_2h
        self.rent_3h = rent_3h
        self.rent_4h = rent_4h
        self.rent_hotel = rent_hotel
        self.house_price = house_price
        self.houses = 0

    def get_rent(self):
        if self.houses == 0:
            # TODO: if all of color group are owned and properties are unimproved,
            # return self.rent * 2
            return self.rent
        if self.houses == 1:
            return self.rent_1h
        if self.houses == 2:
            return self.rent_2h
        if self.houses == 3:
            return self.rent_3h
        if self.houses == 4:
            return self.rent_4h
        if self.houses == 5:
            return self.rent_hotel

    def on_land(self, player):
        super(ColorProperty, self).on_land(player)

    def add_house(self):
        self.houses += 1
        self.owner.make_payment(self.house_price)

    def sell_house(self):
        self.houses -= 1
        self.owner.receive_payment(self.house_price / 2)

    
    
