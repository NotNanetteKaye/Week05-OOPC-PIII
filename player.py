import time

class Player:
    def __init__(self, name):
        self.name = name
        self.gesture = None
        self.gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.points = 0
        pass

    def player_chooses(self):
        print("")
        print("Choose your gesture.")
        time.sleep(1)
        print("Enter 0 for Rock")
        time.sleep(1)
        print("Enter 1 for Paper")
        time.sleep(1)
        print("Enter 2 for Scissors")
        time.sleep(1)
        print("Enter 3 for Lizard")
        time.sleep(1)
        print("Enter 4 for Spock")
        print("")
        self.gesture = int(input("Please enter your gesture: "))
        pass
