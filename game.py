###Main Interface
from asset_creator import AssetCreator

class RunGame:
    def __init__(self) -> None:
        self.round_count = 0
        self.game_continue = True
        self.creator = AssetCreator()
        self.player_one = None


    def run_game(self):
        play_again = True
        while play_again:
            self.game_mode()
            self.asset_creation()
            self.ship_placement()
            while self.game_continue:
                self.player_turn()
        play_again = input("Do you wish to play again? Yes or No: ")        

    def game_mode(self):
        self.mode = input("Which game mode would you like to player?\n1: Single Player 2: Multiplayer\n ")

    def asset_creation(self):
        # self.creator.ship_creator.fleet_creator()
        self.creator.create_players(self.mode)

    def ship_placement(self):
        for player in self.creator.players:
            ships_placed = 0
            while ships_placed < 5:
                player.ship_tracker_board.print_board()
                player.place_ship()
                ships_placed += 1

    def player_turn(self):
        for player in self.creator.players:
            player.attack_position
            self.win_condition_check()

    def win_condition_check(self):
        pass
