##Creates ships for the players
from battleship import Battleship
from carrier import AircraftCarrier
from submarine import Submarine
from destroyer import Destroyer


class ShipCreator:
    def __init__(self):
        self.health = 0
        self.grid_location = []
        self.destroyed = False


    def battleship_creator(self):
        Battleship()

    def carrier_creator(self):
        AircraftCarrier()

    def submarine_creator(self):
        Submarine()

    def destroyer_creator(self):
        Destroyer()