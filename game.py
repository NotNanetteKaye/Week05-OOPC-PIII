from ai import AI

class Game:
    def __init__(self):
        self.player1= None
        self.player2 = None
        pass

    def display_welcome(self):
        print("Welcome to Rock Paper Scissors Lizard Spock!")
        print("Each match will be best of three games.")
        print("Use the number keys to enter your selection.")
        pass

    def user_input(self):
        user_input= int(input("1: single-player 2: multi-player"))
        if user_input == 1:
            self.player1= AI("Player1")
            self.player2 = AI("Player2")
        elif user_input == 2:
            self.player1= AI("Player1")
            self.player2 = AI("Player2")
        else:
            print("Please enter 1 or 2.")
        pass

    def run_game(self):
        self.display_welcome()
        self.user_input()
        pass