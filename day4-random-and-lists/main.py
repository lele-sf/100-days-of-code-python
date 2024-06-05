import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_images = [rock, paper, scissors]

while True:
    choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    if choice < 0 or choice > 2:
        print("Invalid input. You must enter 0, 1, or 2.")
        continue
    break

random_choice = random.randint(0, 2)
outcome = ''

if choice == random_choice:
    outcome = "Draw!"
elif choice - random_choice == 2 or choice - random_choice == -1:
    outcome = "You lose!"
else:
    outcome = "You win!"

user_choice = game_images[choice]
computer_choice = game_images[random_choice]

print(user_choice)
print("Computer chose:\n", computer_choice)
print(outcome)
