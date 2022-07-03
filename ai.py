from random import randint
from player import Player

class AI(Player):
    def __init__(self, name):
        super().__init__(name)
    pass

    def games_begin(self):
        gesture_choice = self.gesture_list[randint(0,4)]
        print(f"{self.name} choose {gesture_choice}!")


