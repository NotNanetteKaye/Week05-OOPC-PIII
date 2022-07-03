from ai import AI
import time

class Game:
    def __init__(self):
        self.player1= None
        self.player2 = None
        pass

    def display_welcome(self):
        print("Welcome to Rock Paper Scissors Lizard Spock!")
        print("Each match will be best of three games.")
        print("Use the number keys to enter your selection.")
        print("")
        pass

    def display_rules(self):
        print("Rock crushes Scissors")
        print("Scissors cuts Paper")
        print("Paper covers Rock")
        print("Rock crushes Lizard")
        print("Lizard poisons Spock ")
        print("Spock smashes Scissors")
        print("Scissors decapitates Lizard")
        print("Lizard eats Paper")
        print("Paper disproves Spock")
        print("Spock vaporizes Rock")
        print("")
        time.sleep(1)
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
        self.display_rules()
        self.user_input()
        pass