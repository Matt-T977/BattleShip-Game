##Creates ships for the players
from battleship import Battleship
from carrier import AircraftCarrier
from submarine import Submarine
from destroyer import Destroyer


class ShipCreator:
    def __init__(self):
        self.fleet_list
        self.fleet_creator()
        pass


    def fleet_creator(self):
        battleship_one = Battleship()
        battleship_two = Battleship()
        carrier = AircraftCarrier()
        submarine = Submarine()
        destroyer = Destroyer()
        self.fleet = [battleship_one, battleship_two, carrier, submarine, destroyer]
        pass