##Destroyer character sheet
from ship_creator import ShipCreator


class Destroyer(ShipCreator):
    def __init__(self):
        super().__init__()
        self.name = "Destroyer"
        self.marker = "D"
        self.health = 2