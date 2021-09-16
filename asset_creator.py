###Player Factory###
from player import Player
from Ai import AI
from ship_creator import ShipCreator
import user_interface


class AssetCreator:
    def __init__(self):
        self.players = []
        self.fleet = []
        self.ship_creator = ShipCreator()
        

    def create_players(self, mode):
        if mode == "2":
            player_one = Player("Player One")
            player_two = Player("Player Two")
        elif mode == "1":
            player_one = Player("Player One")
            player_two = AI("AI")    
        self.players = [player_one, player_two]
        self.player_hit_tracker_board()
        self.player_ship_tracker_board()

    def fleet_creator(self):
        battleship_one = self.ship_creator.battleship_creator()
        battleship_two = self.ship_creator.battleship_creator()
        carrier = self.ship_creator.carrier_creator()
        submarine = self.ship_creator.submarine_creator()
        destroyer = self.ship_creator.destroyer_creator()
        self.fleet = [battleship_one, battleship_two, carrier, submarine, destroyer]
    