###Main Interface
from player_creator import PlayerCreator

class RunGame:
    def __init__(self) -> None:
        self.round_count = 0
        self.game_continue = True
        self.creator = PlayerCreator()

    def run_game(self):
        self.game_mode()
        self.player_creation()

    def game_mode(self):
        self.mode = input("Which game mode would you like to player?\n1: Single Player 2: Multiplayer\n ")

    def player_creation(self):
        self.creator.fleet_creator()
        self.creator.create_players(self.mode)
        self.creator.players[0].player_hit_tracker_board()
        self.creator.players[0].player_ship_tracker_board()
        self.creator.players[1].player_hit_tracker_board()
        self.creator.players[1].player_ship_tracker_board()


    def ship_placement(self):
        pass

    def player_turn(self, player):
        pass

    def win_condition_check(self):
        pass
