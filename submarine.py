##Submarine character sheet
from ship_creator import ShipCreator


class Submarine(ShipCreator):
    def __init__(self):
        super().__init__()
        self.name = "Submarine"
        self.marker = "S"
        self.health = 3