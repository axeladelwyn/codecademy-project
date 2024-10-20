# Text-Based Adventure Game on Terminal Using Python

# One interactive feature using Input()
# Use Git version control
# Use the command lin and file navigation
# Write a technical blog post on the project

# I wanted the program to be an adventure game, you could pick a choice
# You can pick choice of regarding what to do by typing in the terminal(using prebuilt tempate)
# Its for one player

class AdventureGame:
    def __init__(self):
        self.playing = True
    def start_game(self):
        print("""You are an adventurer in a world of danger. Pick your choice carefully, and you might survive...
        Press any key to continue""")
        input()
        self.main_adventure()
    def main_adventure(self):
        # loops the game while playing is true
        while self.playing:
            self.cave_choice()

    def cave_choice(self):
        print("You entered a dark cave. What should you do?")
        cave = input("1. Explore the cave.\n2. Gather a party first and then come back to explore.\n3. Quit the game.\nEnter your choice: ")

        if cave == "1":
            self.explore_cave()
        elif cave == "2":
            self.gather_party()
        elif cave == "3":
            print("You chose to quit the game. Farewell, adventurer!")
            self.playing = False
        else:
            print("Invalid choice. Please select a valid option.")

    def explore_cave(self):
        while True:
            print("You found a bear sleeping inside! What should you do?")
            action = input("1. Try to sneak past it.\n2. Attack the bear.\n3. Run away.\nEnter your choice: ")

            if action == "1":
                print("You managed to sneak past the bear and found a hidden treasure!")
                print("Inside the treasure, you find a mysterious artifact that grans you the power of eternal life")
                print("Congratulations, you have achieved the ultimate victory and completed the game")
                playing = False
                break  # Exit the loop for this scenario
            elif action == "2":
                print("The bear woke up and fought back. You were defeated. Game over.")
                playing = False  # End the game
                break
            elif action == "3":
                print("You ran out of the cave safely, but you missed the chance to explore further.")
                break
            else:
                print("Invalid choice. Please choose a valid option.")  # Stay in the loop if input is invalid

    def gather_party(self):
        print("You gathered a party and returned to the cave. Together, you managed to defeat the bear and found a treasure chest!")
        self.choose_weapon()

    def choose_weapon(self):
        print("What weapon should you pick from the treasure chest?")
        treasure_input = input("1. Sword\n2. Bow\nEnter your choice: ")
        if treasure_input == "1":
            print("You take the sword and are ready for a new adventure!")
        elif treasure_input == "2":
            print("You take the bow and are ready for a new adventure!")
        else:
            print("Invalid choice. Please select a valid option.")

        # Continue the adventure after choosing the weapon
        self.next_adventure()

    def next_adventure(self):
        print("You gain an experience from last cave encounter, now you set on your own adventure on your own without a party to help you out!")
        while True:
            adventure = input("1. Choose to take an adventure in the desert.\n2. Choose to take an adventure in the forest.\nEnter your choice: ")
            if adventure == "1":
                self.adventure_desert()
                break
            elif adventure == "2":
                self.adventure_forest()
                break
            else:
                print("Invalid choice. Please choose a valid option.")

    def adventure_desert(self):
        print("You venture into the desert and face a scorching sun and a lurking sandworm!")
        desert_action = input("1. Fight the sandworm.\n2. Hide and wait for it to pass.\nEnter your choice: ")
        if desert_action == "1":
            print("You bravely fight the sandworm and emerge victorious! The people of the desert crown you as a hero.")
            print("Congratulations, you have completed the game with honor!")
        elif desert_action == "2":
            print("You hide, but the sandworm senses your presence and attacks. You couldn't escape in time. Game over.")
        self.playing = False

    def adventure_forest(self):
        print("You explore the forest, where you encounter mystical creatures and a hidden ancient ruin.")
        forest_action = input("1. Investigate the ancient ruin.\n2. Follow the mystical creatures deeper into the forest.\nEnter your choice: ")
        if forest_action == "1":
            print("Inside the ruin, you find an enchanted shield that protects you from any harm. You have found a powerful artifact and won the game!")
        elif forest_action == "2":
            print("The creatures lead you into a trap, where you get lost in the magical forest forever. Game over.")
        self.playing = False

if __name__ == "__main__":
    game = AdventureGame()
    game.start_game()
    
    print("The adventure ends here. Thanks for playing!")