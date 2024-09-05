import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()


def play_game(difficulty):
    number_to_guess = random.randint(1, 100)
    print(number_to_guess)

    def game_level(attempts):
        while attempts != 0:
            attempts -= 1
            guess = int(input("Make a guess: "))
            if guess == number_to_guess:
                print("You guessed right! Congratulations!")
                attempts = 0
            if attempts == 0 and guess != number_to_guess:
                print("You've used all the attempts. You lose!")
            elif guess + 20 < number_to_guess:
                print("Too low")
            elif guess - 20 > number_to_guess:
                print("Too high")

    if difficulty == "easy":
        print(f"You have chosen difficulty level {difficulty}. You have 10 attempts. Good Luck!")
        game_level(10)

    elif difficulty == "hard":
        print(f"You have chosen difficulty level {difficulty}. You have 5 attempts. Good Luck!")
        game_level(5)

    else:
        print("You did not provide a valid answer.")

play_game(level)