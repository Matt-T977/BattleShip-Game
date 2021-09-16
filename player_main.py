import user_interface
from board import Board


class PlayerMain:
    def __init__(self, name) -> None:
        self.name = name
        self.hit_tracker_board = Board("Hit Tracker")
        self.ship_tracker_board = Board("Ship Tracker")
    

    def attack_position(self):
        attack_grid = user_interface.position_input_format()
        
    def place_ship(self):
        pass    

    def display_remaining_ships(self):
        pass