###Player Factory###
from player import Player
from Ai import AI
from ship_creator import ShipCreator


class PlayerCreator:
    def __init__(self):
        self.players = []
        self.ship_creator = ShipCreator()
        pass
        

    def create_players(self, mode):
        if mode == "2":
            player_one = Player("Player One")
            player_two = Player("Player Two")
        elif mode == "1":
            player_one = Player("Player One")
            player_two = AI("AI")    
        self.players = [player_one, player_two]
        pass

    