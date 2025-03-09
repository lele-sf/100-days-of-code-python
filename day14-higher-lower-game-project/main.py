import random
import os
from game_data import data
from art import logo, vs

score = 0
first_choice = random.choice(data)

while True:
    print(logo)
    second_choice = random.choice(data)

    while first_choice == second_choice:
        second_choice = random.choice(data)

    print(
        f"Compare A: {first_choice['name']}, {first_choice['description']}, from {first_choice['country']}."
    )
    print(vs)
    print(
        f"Against B: {second_choice['name']}, {second_choice['description']}, from {second_choice['country']}."
    )

    guess = input("Who has more followers? Type 'A' or 'B': ").upper().strip()

    correct_answer = (
        "A" if first_choice["follower_count"] > second_choice["follower_count"] else "B"
    )

    if guess == correct_answer:
        score += 1
        print(f"Correct! Your score is {score}.\n")
        os.system("cls")
        first_choice = first_choice if correct_answer == "A" else second_choice
    else:
        print(f"LOST! Final score: {score}")
        break
