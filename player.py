###Human Player Controls
from player_creator import PlayerCreator


class Player(PlayerCreator):
    def __init__(self, name):
        super().__init__(name)
    

    def display_remaining_ships(self):
        pass