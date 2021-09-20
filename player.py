###Human Player Controls
import user_interface
from board import Board
from ship_creator import ShipCreator


class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.fleet = ShipCreator()
        self.hit_tracker_board = Board("Hit Tracker")
        self.ship_tracker_board = Board("Ship Tracker")
        pass


    def attack_position(self):
        attack_grid = user_interface.position_input_format()
        pass

    def place_ship(self, ship):
        ship_size = self.fleet.fleet_list[ship].health
        placement_direction = input("Do you wish to place your ship horizontal or vertical? 1: horizontal 2: vertical\n")
        if placement_direction == "1":
            position_list = user_interface.position_input_format()
            

        pass

    def display_remaining_ships(self):
        pass