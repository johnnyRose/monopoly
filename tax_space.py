class TaxSpace():
    def __init__(self, name, income_tax):
        self.name = name
        self.income_tax = income_tax

    def on_land(self, player):
        print(self.name + "!")
        if (self.income_tax):
            tenPercent = player.cash / 10
            if tenPercent > 200:
                player.make_payment(tenPercent) # 10% or $200
            else:
                player.make_payment(200)
        else:
            player.make_payment(75) # luxury tax
