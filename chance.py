import random

class Chance():

    # TODO: finish results of all "Advance To ..." cards
    def on_land(self, player, board):
        print("Chance!")
        self.player = player
        self.board = board
        self._draw_card()

    def _draw_card(self):
        cards = [
            self._advance_to_illinois,
            self._advance_to_st_charles,
            self._go_back_3_spaces,
            self._get_out_of_jail_free,
            self._advance_to_nearest_utility,
            self._poor_tax,
            self._advance_to_reading,
            self._chairman_of_board,
            self._general_repairs,
            self._advance_to_go,
            self._building_and_loan_matures,
            self._advance_to_boardwalk,
            self._bank_pays_dividend,
            self._advance_to_nearest_railroad, # This card exists twice.
            self._advance_to_nearest_railroad,
            self._go_to_jail,
            ]

        index = random.randrange(0, len(cards))
        cards[index]()

    def _advance_to_illinois(self):
        print("Advance to Illinois Avenue! If you pass Go, collect $200!")

    def _advance_to_st_charles(self):
        print("Advance to St. Charles Place! If you pass Go, collect $200!")

    def _go_back_3_spaces(self):
        print("Go back 3 spaces!")

    def _get_out_of_jail_free(self):
        print("Get out of jail, free!")
        self.player.get_out_of_jail_free_cards += 1

    def _advance_to_nearest_utility(self):
        print("Advance token to nearest utility! " +
              "If unowned, you may buy it from the bank. " +
              "If owned, throw dice and pay owner a total " +
              "of ten times the amount thrown.")

    def _poor_tax(self):
        print("Pay poor tax of $15!")
        self.player.make_payment(15)

    def _advance_to_reading(self):
        print("Take a ride on the Reading! If you pass go, collect $200!")

    def _chairman_of_board(self):
        print("You have been elected chairman of the board! " +
              "Pay each player $50!")
        for player in self.board.players:
            self.player.make_payment(50, player)

    def _general_repairs(self):
        print("Make general repairs on all your property! " +
              "For each house pay $25, for each hotel pay $100!")
        cost = self.player.get_street_repair_cost(True)
        self.player.make_payment(cost)

    def _advance_to_go(self):
        print("Advance to Go! Collect $200!")
        self.player.current_space = 0;
        self.player.receive_payment(200)

    def _building_and_loan_matures(self):
        print("Your building and loan matures! Collect $150!")
        self.player.receive_payment(150)

    def _advance_to_boardwalk(self):
        print("Take a walk on the Boardwalk! Advance token to Boardwalk!")
        pass

    def _bank_pays_dividend(self):
        print("Bank pays you dividend of $50!")
        self.player.receive_payment(50)

    # This card exists twice in the Chance deck.
    def _advance_to_nearest_railroad(self):
        print("Advance token to the nearest railroad and pay owner " +
              "twice the Rental to which he is otherwise entitled. " +
              "If railroad is unowned, you may buy it from the bank.")

    def _go_to_jail(self):
        print("Go directly to jail! Do not pass Go, " + 
              "do not collect $200!")
        self.player.go_to_jail()
