import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")


user_cards = [random.choice(cards), random.choice(cards)]
comp_cards = [random.choice(cards), random.choice(cards)]

def game():
    print(logo)
    user_current_score = sum(user_cards)
    comp_current_score = sum(comp_cards)
    if 11 in user_cards and user_current_score > 21:
        user_current_score -= 10
    print(f"Your cards: {user_cards}, current score: {user_current_score}")
    print(f"Computer's first card: {comp_cards[0]}")
    if user_current_score > 21 or 11 in comp_cards:
        print("Game Over! Either your score was greater than 21 or the Computer had a black jack. 🥲")
    else:
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if another_card == "n":
            print(f"Your final hand: {user_cards}, final score: {user_current_score} ")
            print(f"Computer's final hand: {comp_cards}, final score: {comp_current_score} ")
            if user_current_score == comp_current_score:
                print("Draw 🙃")
            elif user_current_score < 21 and user_current_score > comp_current_score:
                print("You win!")
            elif comp_current_score < 21 and comp_current_score > user_current_score:
                print("You lose!")
            elif user_current_score > 21:
                print("You lose!")
            elif 11 in user_cards:
                print("You win! You have a black jack!")
            elif 11 in user_cards and 10 in comp_cards:
                print("You lose! Computer also has a black jack!")


        elif another_card == 'y':
            user_cards.append(random.choice(cards))
            comp_cards.append((random.choice(cards)))
            game()


if play_game == 'y':
    game()




