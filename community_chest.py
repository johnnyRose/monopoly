import random

class CommunityChest():

    def on_land(self, player, board):
        print("Community Chest!")
        self.player = player
        self.board = board
        self._draw_card()

    def _draw_card(self):
        cards = [
            self._go_to_jail,
            self._inherit_100,
            self._receive_for_services,
            self._get_out_of_jail_free,
            self._from_sale_of_stock,
            self._collect_50_from_every_player,
            self._income_tax_refund,
            self._doctors_fee,
            self._second_prize,
            self._advance_to_go,
            self._street_repairs,
            self._christmas_fund_matures,
            self._bank_error,
            self._pay_hospital,
            self._pay_school_tax,
            self._life_insurance_matures,
            ]

        index = random.randrange(0, len(cards))
        cards[index]()

    def _go_to_jail(self):
        print("Go directly to jail! Do not pass Go, " + 
              "do not collect $200!")
        self.player.go_to_jail()

    def _inherit_100(self):
        print("You inherit $100!")
        self.player.receive_payment(100)

    def _receive_for_services(self):
        print("Receive for services $25!")
        self.player.receive_payment(25)

    def _get_out_of_jail_free(self):
        print("Get out of jail, free!")
        self.player.get_out_of_jail_free_cards += 1

    def _from_sale_of_stock(self):
        print("From sale of stock, you get $45!")
        self.player.receive_payment(45)

    def _collect_50_from_every_player(self):
        print("Grand opera opening! Collect $50 from every player " +
              "for opening night seats!")
        for player in self.board.players:
            player.make_payment(50, self.player)

    def _income_tax_refund(self):
        print("Income tax refund, collect $20!")
        self.player.receive_payment(20)

    def _doctors_fee(self):
        print("Doctor's fee! Pay $50!")
        self.player.make_payment(50)

    def _second_prize(self):
        print("You have won second prize in a beauty contest! " +
              "Collect $10!")
        self.player.receive_payment(10)

    def _advance_to_go(self):
        print("Advance to Go! Collect $200!")
        self.player.current_space = 0;
        self.player.receive_payment(200)

    def _street_repairs(self):
        print("You are assessed for street repairs! " +
              "Pay $40 per hours and $115 per hotel!")
        cost = self.player.get_street_repair_cost()
        self.player.make_payment(cost)

    def _christmas_fund_matures(self):
        print("Christmas fund matures! Collect $100!")
        self.player.receive_payment(100)

    def _bank_error(self):
        print("Bank error in your favor! Collect $200!")
        self.player.receive_payment(200)

    def _pay_hospital(self):
        print("Pay hospital $100!")
        self.player.make_payment(100)

    def _pay_school_tax(self):
        print("Pay school tax of $150!")
        self.player.make_payment(150)

    def _life_insurance_matures(self):
        print("Life insurance matures! Collect $100!")
        self.player.receive_payment(100)
