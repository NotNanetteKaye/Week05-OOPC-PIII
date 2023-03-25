from ai import AI
import time

from human import Human

class Game:
    def __init__(self):
        self.player1= None
        self.player2 = None
        pass

    def display_welcome(self):
        print("\nWelcome to Rock Paper Scissors Lizard Spock!\nEach match will be best of three games.\nUse the number keys to enter your selection.\n\n")

        pass

    def display_rules(self):
        time.sleep(.25)
        print("Rock crushes Scissors")
        time.sleep(.25)
        print("Scissors cuts Paper")
        time.sleep(.25)
        print("Paper covers Rock")
        time.sleep(.25)
        print("Rock crushes Lizard")
        time.sleep(.25)
        print("Lizard poisons Spock ")
        time.sleep(.25)
        print("Spock smashes Scissors")
        time.sleep(.25)
        print("Scissors decapitates Lizard")
        time.sleep(.25)
        print("Lizard eats Paper")
        time.sleep(.25)
        print("Paper disproves Spock")
        time.sleep(.25)
        print("Spock vaporizes Rock\n")
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
            print("\nInvalid option.\nPlease try again\n")
            self.game_mode()
        pass

    def player_chooses_rock(self):
        if self.player1.gesture == 0 and (self.player2.gesture == 2 or self.player2.gesture == 3):
            self.player1.points += 1
            print(f"\n{self.player1.gesture_choice} crushes {self.player2.gesture_choice}!")
            print(f"{self.player1.name} wins!\n")
        elif self.player2.gesture == 0 and (self.player1.gesture == 2 or self.player1.gesture == 3):
                self.player2.points += 1
                print(f"\n{self.player2.gesture_choice} crushes {self.player1.gesture_choice}!")
                print(f"{self.player2.name} wins!\n")
        pass

    def player_chooses_paper(self):
        if self.player1.gesture == 1 and (self.player2.gesture == 0 or self.player2.gesture == 4):
            self.player1.points += 1
            print(f"\n{self.player1.gesture_choice} {'covers' if self.player2.gesture == 0 else 'disproves'} {self.player2.gesture_choice}!")
            print(f"{self.player1.name} wins!\n")
        elif self.player2.gesture == 1 and (self.player1.gesture == 0 or self.player1.gesture == 4):
            self.player2.points += 1
            print(f"\n{self.player2.gesture_choice} {'covers' if self.player1.gesture == 0 else 'disproves'} {self.player1.gesture_choice}!")
            print(f"{self.player2.name} wins!\n")
        pass
    
    def player_chooses_scissors(self):
        if self.player1.gesture == 2 and (self.player2.gesture == 1 or self.player2.gesture == 3):
            self.player1.points += 1
            print(f"\n{self.player1.gesture_choice} {'cut' if self.player2.gesture == 1 else 'decapitate'} {self.player2.gesture_choice}!")
            print(f"{self.player1.name} wins!\n")
        elif self.player2.gesture == 2 and (self.player1.gesture == 1 or self.player1.gesture == 3):
            self.player2.points += 1
            print(f"\n{self.player2.gesture_choice} {'cut' if self.player1.gesture == 1 else 'decapitate'} {self.player1.gesture_choice}!")
            print(f"{self.player2.name} wins!\n")
        pass

    def player_chooses_lizard(self):  
        if self.player1.gesture == 3 and (self.player2.gesture == 4 or self.player2.gesture == 1):
            self.player1.points += 1
            print(f"\n{self.player1.gesture_choice} {'poisons' if self.player2.gesture == 4 else 'eats'} {self.player2.gesture_choice}!")
            print(f"{self.player1.name} wins!\n")
        elif self.player2.gesture == 3 and (self.player1.gesture == 4 or self.player1.gesture == 1):
            self.player2.points += 1
            print(f"\n{self.player2.gesture_choice} {'poisons' if self.player1.gesture == 4 else 'eats'} {self.player1.gesture_choice}!")
            print(f"{self.player2.name} wins!\n")
        pass 

    def player_chooses_spock(self):
        if self.player1.gesture == 4 and (self.player2.gesture == 2 or self.player2.gesture == 0):
            self.player1.points += 1
            print(f"\n{self.player1.gesture_choice} {'smashes' if self.player2.gesture == 2 else 'vaporizes'} {self.player2.gesture_choice}!")
            print(f"{self.player1.name} wins!\n")
        elif self.player2.gesture == 4 and (self.player1.gesture == 2 or self.player1.gesture == 0):
            self.player2.points += 1
            print(f"\n{self.player2.gesture_choice} {'smashes' if self.player1.gesture == 2 else 'vaporizes'}  {self.player1.gesture_choice}!")
            print(f"{self.player2.name} wins!\n")
        pass

    def battlefield(self):
        while self.player1.points < 2 and self.player2.points < 2:
            self.player1.player_chooses()
            self.player2.games_begin()
            if self.player1.gesture != self.player2.gesture:
                self.player_chooses_rock()
                self.player_chooses_paper()
                self.player_chooses_scissors()
                self.player_chooses_lizard()
                self.player_chooses_spock()
            else:
                print('A tie! No points awarded')

    def display_winner(self):
        if self.player1.points == self.player2.points:
            print("No winner!")
        else:
            print(f"Congratulations! {self.player1.name if self.player1.points > self.player2.points else self.player2.name} wins the game of Rock, Paper, Scissor, Lizard, Spock!")
        pass

    def play_again(self):
        user_input = (input("Would you like to play again? Enter y/n "))
        if user_input == "y" or user_input == "n":
            if user_input == "y":
                self.run_game()
            elif user_input == "n":
                print("Okay!")
            else:
                print("Invalid option.\nPlease choose a proper option")
                self.play_again() 
        pass

    def run_game(self):
        self.display_welcome()
        self.display_rules()
        self.game_mode()
        self.battlefield()
        self.display_winner()
        self.play_again()
        pass