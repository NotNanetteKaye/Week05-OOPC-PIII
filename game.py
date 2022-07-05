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

    def player_chooses_rock(self):
        if self.player1.points <= 2 and self.player2.points <= 2:
            if self.player1.gesture == 0 and (self.player2.gesture == 2 or self.player2.gesture == 3):
                self.player1.points += 1
                print("")
                print(f"{self.player1.gesture_choice} crushes {self.player2.gesture_choice}!")
                print(f"{self.player1.name} wins!")
                print("")
            elif self.player2.gesture == 0 and (self.player1.gesture == 2 or self.player1.gesture == 3):
             self.player2.points += 1
             print("")
             print(f"{self.player2.gesture_choice} crushes {self.player1.gesture_choice}!")
             print(f"{self.player2.name} wins!")
             print("")
        else:
            print("A tie! No points awarded.")
            self.battlefield()
        pass

    def player_chooses_paper(self):
        if self.player1.points <= 2 and self.player2.points <= 2:
            if self.player1.gesture == 1 and self.player2.gesture == 0:
                self.player1.points += 1
                print("")
                print(f"{self.player1.gesture_choice} covers {self.player2.gesture_choice}!")
                print(f"{self.player1.name} wins!")
                print("")
            elif self.player2.gesture == 1 and self.player1.gesture == 0:
                self.player2.points += 1
                print("")
                print(f"{self.player2.gesture_choice} covers {self.player1.gesture_choice}!")
                print(f"{self.player2.name} wins!")
                print("")
            elif self.player1.gesture == 1 and self.player2.gesture == 4:
             self.player1.points += 1
             print("")
             print(f"{self.player1.gesture_choice} disproves {self.player2.gesture_choice}!")
             print(f"{self.player1.name} wins!")
             print("")
            elif self.player2.gesture == 1 and self.player1.gesture == 4:
             self.player2.points += 1
             print("")
             print(f"{self.player2.gesture_choice} disproves {self.player1.gesture_choice}!")
             print(f"{self.player2.name} wins!")
             print("")
        else:
            print("A tie! No points awarded.")
            self.battlefield()
        pass
    
    def player_chooses_scissors(self):
        if self.player1.points <= 2 and self.player2.points <= 2:
            if self.player1.gesture == 2 and self.player2.gesture == 1:
                self.player1.points += 1
                print("")
                print(f"{self.player1.gesture_choice} cut {self.player2.gesture_choice}!")
                print(f"{self.player1.name} wins!")
                print("")
            elif self.player2.gesture == 2 and self.player1.gesture == 1:
                self.player2.points += 1
                print("")
                print(f"{self.player2.gesture_choice} cut {self.player1.gesture_choice}!")
                print(f"{self.player2.name} wins!")
                print("")
            elif self.player1.gesture == 2 and self.player2.gesture == 3:
             self.player1.points += 1
             print("")
             print(f"{self.player1.gesture_choice} decapitate {self.player2.gesture_choice}!")
             print(f"{self.player1.name} wins!")
             print("")
            elif self.player2.gesture == 2 and self.player1.gesture == 3:
             self.player2.points += 1
             print("")
             print(f"{self.player2.gesture_choice} decapitate {self.player1.gesture_choice}!")
             print(f"{self.player2.name} wins!")
             print("")
        else:
            print("A tie! No points awarded.")
            self.battlefield()
        pass

    def player_chooses_lizard(self):  
        if self.player1.points <= 2 and self.player2.points <= 2:
            if self.player1.gesture == 3 and self.player2.gesture == 4:
                self.player1.points += 1
                print("")
                print(f"{self.player1.gesture_choice} poisons {self.player2.gesture_choice}!")
                print(f"{self.player1.name} wins!")
                print("")
            elif self.player2.gesture == 3 and self.player1.gesture == 4:
                self.player2.points += 1
                print("")
                print(f"{self.player2.gesture_choice} poisons {self.player1.gesture_choice}!")
                print(f"{self.player2.name} wins!")
                print("")
            elif self.player1.gesture == 3 and self.player2.gesture == 1:
             self.player1.points += 1
             print("")
             print(f"{self.player1.gesture_choice} eats {self.player2.gesture_choice}!")
             print(f"{self.player1.name} wins!")
             print("")
            elif self.player2.gesture == 3 and self.player1.gesture == 1:
             self.player2.points += 1
             print("")
             print(f"{self.player2.gesture_choice} eats {self.player1.gesture_choice}!")
             print(f"{self.player2.name} wins!")
             print("")
        else:
            print("A tie! No points awarded.")
            self.battlefield()
        pass 

    def battlefield(self):
        self.player1.player_chooses()
        self.player2.games_begin()
        pass

    def display_winner(self):
        if self.player1.points == 2:
            print(f"Congratulations! {self.player1.name} won best of 3!")
        if self.player2.points == 2:
            print(f"Congratulations! {self.player2.name} won best of 3!")

    def play_again(self):
        user_input = (input("Would you like to play again? Enter y/n "))
        if user_input == "y" or user_input == "n":
            if user_input == "y":
                self.run_game()
            elif user_input == "n":
                print("Okay!")
            else:
                print("Invalid option.")
                print("Please choose a proper option.")
                self.play_again() 
        pass

    def run_game(self):
        self.display_welcome()
        # self.display_rules()
        self.game_mode()
        self.battlefield()
        self.display_winner()
        # self.play_again()
        pass