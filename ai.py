from random import randint
from player import Player

class AI(Player):
    def __init__(self, name):
        super().__init__(name)
        pass

    def games_begin(self):
        self.gesture = randint(0,4)
        self.gesture_choice = self.gesture_list[self.gesture]
        print(f"{self.name} choose {self.gesture_choice}!")
        pass


