##Aircraft Carrier character sheet
from ship_main import ShipMain


class AircraftCarrier(ShipMain):
    def __init__(self):
        super().__init__()
        self.name = "Aircraft Carrier"
        self.marker = "C"
        self.health = 5