# The logic controller for the different game elements. 

from board import Board
from dice import Dice
from player import Player

board = Board()

player = Player("John")
dice = Dice();

players = [player]

board.set_players(players)

def jail_logic():
    print("You are in jail!")
    dice.roll()
    if dice.rolled_doubles:
        print("You rolled doubles! You're out of jail!")
        pass
    else:
        print("You did not roll doubles.")

        if player.get_out_of_jail_free_cards > 0:
            prompt = "You have a get out of jail free card. Use it? (y/n)"
        else:
            prompt = "Pay $50 to get out? (y/n)"
            
        response = input(prompt)
        if response == "y":
            player.leave_jail()
        else:
            player.suspended_turns -= 1

for i in range(30):

    if player.suspended_turns > 0:
        jail_logic()
        continue
    
    player.move(dice)
    board.spaces[player.current_space].on_land(player, board)
    double_count = 0
    
    while dice.rolled_doubles:
        double_count += 1
        
        if double_count >= 3:
            player.go_to_jail()
        
        player.move(dice)
        board.spaces[player.current_space].on_land(player, board)

