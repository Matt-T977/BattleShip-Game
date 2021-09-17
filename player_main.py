import user_interface
from board import Board
from ship_creator import ShipCreator


class PlayerMain:
    def __init__(self, name) -> None:
        self.name = name
        self.fleet = ShipCreator()
        self.hit_tracker_board = Board("Hit Tracker")
        self.ship_tracker_board = Board("Ship Tracker")
        pass


    def attack_position(self):
        attack_grid = user_interface.position_input_format()
        pass

    def place_ship(self):
        pass    

    def display_remaining_ships(self):
        pass