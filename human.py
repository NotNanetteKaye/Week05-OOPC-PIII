
from player import Player

class Human(Player):
    def __init__(self, name):
        super().__init__(name)
        pass

    def games_begin(self):
        self.player_chooses()
        pass