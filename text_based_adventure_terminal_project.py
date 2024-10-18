# Text-Based Adventure Game on Terminal Using Python

# One interactive feature using Input()
# Use Git version control
# Use the command lin and file navigation
# Write a technical blog post on the project

# I wanted the program to be an adventure game, you could pick a choice
# You can pick choice of regarding what to do by typing in the terminal(using prebuilt tempate)
# Its for one player

print("""You are an adventurer in a world of danger. Pick your choice carefully, and you might survive...
Press any key to continue""")
input()

playing = True  # A flag to keep the game running
while playing:
    print("You entered a dark cave. What should you do?")
    cave = input("1. Explore the cave.\n2. Gather a party first and then come back to explore.\n3. Quit the game.\nEnter your choice: ")

    if cave == "1":
        while True:  # Loop to allow multiple choices in this scenario
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

    elif cave == "2":
        print("You gathered a party and returned to the cave. Together, you managed to defeat the bear and found a treasure chest!")
        # The game can continue or end here, as desired
        print("What weapon should you pick from treasure chest?")
        treasure_input = input("1. Sword\n 2.Bow\n")
        if treasure_input == "1":
            print("You take the sword and ready for new adventure!")
        elif treasure_input == "2":
            print("You take the bow and ready for new adventure!")
        else:
            print("Invalid choice. Please select a valid option.")
        # Continue the adventure after choosing the weapon
        print("You gain an experience from last cave encounter, now you set on your own adventure on your own without a party to help you out!")

        while True:
            adventure = input("1.Choose to take an adventure in the desert\n 2.Choose to take adventure in the forest")
            if adventure == "1":
                print("You venture into the desert and face a scorching sun and a lurking sandworm!")
                desert_action = input("1. Fight the sandworm.\n2. Hide and wait for it to pass.\nEnter your choice: ")
                break
            elif adventure == "2":
                print("You hide, but the sandworm senses your presence and attacks. You couldn't escape in time. Game over.")
                playing = False
                break
            else:
                print("Invalid choice. Please select a valid option.")


    elif cave == "3":
        print("You chose to quit the game. Farewell, adventurer!")
        playing = False  # End the game

    else:
        print("Invalid choice. Please select a valid option.")  # Prompt the user to choose again

print("The adventure ends here. Thanks for playing!")