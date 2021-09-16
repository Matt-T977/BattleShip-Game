##Submarine character sheet
from ship_main import ShipMain


class Submarine(ShipMain):
    def __init__(self):
        super().__init__()
        self.name = "Submarine"
        self.marker = "S"
        self.health = 3