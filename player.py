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
        # time.sleep(1)
        print("Enter 0 for Rock")
        # time.sleep(1)
        print("Enter 1 for Paper")
        # time.sleep(1)
        print("Enter 2 for Scissors")
        # time.sleep(1)
        print("Enter 3 for Lizard")
        # time.sleep(1)
        print("Enter 4 for Spock")
        print("")
        player_input = int(input(f"{self.name}, please enter your gesture: "))
        if player_input <= 4 and player_input > -1:
            if player_input <= 4:
                self.gesture = player_input
                self.gesture_choice = self.gesture_list[self.gesture]
                print(f"{self.name} chose {self.gesture_choice}!")
                pass 
            elif player_input > -1:
                self.gesture = player_input
                self.gesture_choice = self.gesture_list[self.gesture]
                print(f"{self.name} chose {self.gesture_choice}!") 
        else:
            print("")
            print("Invalid option.")
            print("Please reinput your gesture choice.")
            self.player_chooses()
        pass






        # elif self.player1.gesture == 1 and (self.player2.gesture == 0 or self.player2.gesture == 4):
        #     self.player1.points += 1
        #         elif (self.player2.gesture )
        #         print("")
        #         print(f"{self.player1.gesture_choice} crushes {self.player2.gesture_choice}!")
        #         print(f"{self.player1.name} wins!")
        #         print("")
        #         self.battlefield()
        #     elif self.player2.gesture == 1 and (self.player1.gesture == 0 or self.player1.gesture == 4):
        #         self.player2.points += 1
        #         print("")
        #         print(f"{self.player2.gesture_choice} crushes {self.player1.gesture_choice}!")
        #         print(f"{self.player2.name} wins!")
        #         print("")
        #         self.battlefield()
