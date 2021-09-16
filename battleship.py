##Battleship character sheet
from ship_main import ShipMain


class Battleship(ShipMain):
    def __init__(self):
        super().__init__()
        self.name = "Battleship"
        self.marker = "B"
        self.health = 4