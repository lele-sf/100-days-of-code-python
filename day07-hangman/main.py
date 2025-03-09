from random_word import RandomWords
from hangman_art import stages, logo

r = RandomWords()
lives = 7
chosen_word = r.get_random_word()
display = ["_"] * len(chosen_word)
guess_list = []
print(logo)

while "_" in display:
    guess = input("Guess a letter: ").lower()

    if guess not in guess_list:
        guess_list += guess
        if guess in chosen_word:
            for index, letter in enumerate(chosen_word):
                if letter == guess:
                    display[index] = letter
        else:
            lives -= 1
            print(
                f"You guessed the letter {guess}, that's not in the word. You lose a life."
            )
            print(stages[lives])
            if lives == 0:
                print("You lose!")
                break
    else:
        print("You already tried that letter. Try again.")

    print("Current display: ", " ".join(display))

if "_" not in display:
    print("You won!")
