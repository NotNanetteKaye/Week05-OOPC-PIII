from ai import AI

class Game:
    def __init__(self):
        self.player1= None
        self.player2 = None
        pass

    def display_welcome(self):
        print("Welcome to Rock, Paper, Scissor, ")
        pass

    def user_input(self):
        user_input= int(input("1: single-player 2: multi-player"))
        if user_input == 1:
            self.player1= AI("Player1")
            self.player2 = AI("Player2")
        else:
            self.player1= AI("Player1")
            self.player2 = AI("Player2")
        pass

    def run_game(self):
        self.user_input()
        pass