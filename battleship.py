##Battleship character sheet
from ship_creator import ShipCreator


class Battleship(ShipCreator):
    def __init__(self):
        super().__init__()
        self.name = "Battleship"
        self.health = 4