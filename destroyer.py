##Destroyer character sheet
from ship_main import ShipMain


class Destroyer(ShipMain):
    def __init__(self):
        super().__init__()
        self.name = "Destroyer"
        self.marker = "D"
        self.health = 2