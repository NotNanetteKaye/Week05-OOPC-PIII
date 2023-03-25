import time

class Player:
    def __init__(self, name):
        self.name = name
        self.gesture = None
        self.gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.gesture_choice = ""
        self.points = 0
        pass

    def player_chooses(self):
        print("")
        print(f"{self.name}, Choose your gesture.")
        time.sleep(.25)
        print("Enter 0 for Rock")
        time.sleep(.25)
        print("Enter 1 for Paper")
        time.sleep(.25)
        print("Enter 2 for Scissors")
        time.sleep(.25)
        print("Enter 3 for Lizard")
        time.sleep(.25)
        print("Enter 4 for Spock")
        print("")
        player_input = int(input(f"{self.name}, please enter your gesture: "))
        if player_input <= 4 and player_input > -1:
            if player_input <= 4:
                self.gesture = player_input
                self.gesture_choice = self.gesture_list[self.gesture]
                print(f"{self.name} chose {self.gesture_choice}!")
                print("")
                pass 
            elif player_input > -1:
                self.gesture = player_input
                self.gesture_choice = self.gesture_list[self.gesture]
                print(f"{self.name} chose {self.gesture_choice}!") 
                print("")
        else:
            print("")
            print("Invalid option.")
            print("Please reinput your gesture choice.")
            print("")
            self.player_chooses()
        pass

