import random
from art import logo


def play_game(attempts):
    random_number = random.randint(1, 100)

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess < random_number:
            print("Too low.")
        elif guess > random_number:
            print("Too high.")
        else:
            print(f"You got it! The answer was {random_number}")
            return

        attempts -= 1

        if attempts == 0:
            print("You've run out of guesses, you lose.")
        else:
            print("Guess again.")


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == "easy":
    play_game(10)
elif difficulty == "hard":
    play_game(5)
else:
    print(
        "Invalid difficulty level. Please restart the game and choose 'easy' or 'hard'."
    )
