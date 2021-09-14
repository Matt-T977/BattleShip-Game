##Aircraft Carrier character sheet
from ship_creator import ShipCreator


class AircraftCarrier(ShipCreator):
    def __init__(self):
        super().__init__()
        self.name = "Aircraft Carrier"
        self.health = 5