from art import logo
import random


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if play_game == 'y':
    print(logo)

while play_game == "y":
    player_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]

    game_over = False

    while not game_over:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {player_cards}")
        print(f"Computer's first card: {computer_cards[0]}")

        if player_score == 0 or player_score > 21:
            game_over = True
        else:
            get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if get_another_card == "y":
                player_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

    if player_score > 21:
        print("You went over. You lose 😤")
    elif computer_score > 21:
        print("Opponent went over. You win 😁")
    elif player_score == computer_score:
        print("It's a draw 🙃")
    elif player_score == 0:
        print("Win with a Blackjack 😎")
    elif computer_score == 0:
        print("Lose, opponent has Blackjack 😱")
    elif player_score > computer_score:
        print("You win 😃")
    else:
        print("You lose 😤")

    play_game = input(
        "Do you want to play another game of Blackjack? Type 'y' or 'n': "
    )
