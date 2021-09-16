###Player Factory###
from player import Player
from Ai import AI
from ship_creator import ShipCreator
from board import Board
import user_interface


class PlayerCreator:
    def __init__(self):
        self.name = ""
        self.players = []
        self.fleet = []
        self.ship_creator = ShipCreator()
        self.board_creator = Board()
        self.hit_tracker_board = []
        self.ship_tracker_board = []


    def create_players(self, mode):
        if mode == "2":
            player_one = Player("Player One")
            player_two = Player("Player Two")
        elif mode == "1":
            player_one = Player("Player One")
            player_two = AI("AI")
        self.players = [player_one, player_two]    

    def fleet_creator(self):
        battleship_one = self.ship_creator.battleship_creator()
        battleship_two = self.ship_creator.battleship_creator()
        carrier = self.ship_creator.carrier_creator()
        submarine = self.ship_creator.submarine_creator()
        destroyer = self.ship_creator.destroyer_creator()
        self.fleet = [battleship_one, battleship_two, carrier, submarine, destroyer]

    def player_hit_tracker_board(self):
        self.hit_tracker_board = self.board_creator.create_board

    def player_ship_tracker_board(self):
        self.ship_tracker_board = self.board_creator.create_board

    def attack_position(self):
        attack_grid = user_interface.position_input_format()
        

    def place_ship(self):
        pass    