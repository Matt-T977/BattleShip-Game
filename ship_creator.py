##Creates ships for the players
from battleship import Battleship
from carrier import AircraftCarrier
from submarine import Submarine
from destroyer import Destroyer


class ShipCreator:
    def __init__(self):
        pass


    def battleship_creator(self):
        return Battleship()

    def carrier_creator(self):
        return AircraftCarrier()

    def submarine_creator(self):
        return Submarine()

    def destroyer_creator(self):
        return Destroyer()