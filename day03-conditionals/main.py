print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

choice = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\"\n")

if choice == "left":
    lake = input("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n")
    if lake == "wait":
        door = input("You arrive at the island unharmed. There is a house with 3 doors.\nOne red, one yellow and one blue. Which colour do you choose?\n")
        if door == "red":
            print("It's a room full of fire. Game Over.")
        elif door == "blue":
            print("You enter a room of beasts. Game Over.")
        elif door == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("You chose a d. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
