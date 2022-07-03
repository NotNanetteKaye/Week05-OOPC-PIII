from ai import AI
import time

from human import Human

class Game:
    def __init__(self):
        self.player1= None
        self.player2 = None
        pass

    def display_welcome(self):
        print("")
        print("Welcome to Rock Paper Scissors Lizard Spock!")
        print("Each match will be best of three games.")
        print("Use the number keys to enter your selection.")
        print("")
        pass

    def display_rules(self):
        time.sleep(6)
        print("Rock crushes Scissors")
        time.sleep(1)
        print("Scissors cuts Paper")
        time.sleep(1)
        print("Paper covers Rock")
        time.sleep(1)
        print("Rock crushes Lizard")
        time.sleep(1)
        print("Lizard poisons Spock ")
        time.sleep(1)
        print("Spock smashes Scissors")
        time.sleep(1)
        print("Scissors decapitates Lizard")
        time.sleep(1)
        print("Lizard eats Paper")
        time.sleep(1)
        print("Paper disproves Spock")
        time.sleep(1)
        print("Spock vaporizes Rock")
        print("")
        time.sleep(2)
        pass

    def game_mode(self):
        print("Which mode would you like to play?")
        user_input= int(input("Please enter 1 for single-player or 2 for multi-player: "))
        if user_input == 1 or user_input == 2:
            if user_input == 1:
                self.player1= Human("Player 1")
                self.player2 = AI("Robot")
            elif user_input == 2:
                self.player1= Human("Player 1")
                self.player2 = Human("Player 2")
        else:
            print("Invalid option.")
            print("Please try again.")
            self.game_mode()
        pass

    def game_begins(self):
        pass

    def display_winner(self):
        pass

    def run_game(self):
        self.display_welcome()
        # self.display_rules()
        self.game_mode()
        pass