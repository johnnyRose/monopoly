# The logic controller for the different game elements. 

from board import Board
from dice import Dice
from player import Player

board = Board()

player = Player()
dice = Dice();

for i in range(15):
    player.move(dice)
    board.spaces[player.current_space].on_land(player)

