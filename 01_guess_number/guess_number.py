import random
import sys

ANSWERS = [
    "Nice essay, but we just need a simple number!",
    "Nice try! But numbers speak louder than words here.",
    "We love your letters, but right now we only speak math.",
    "Error 404: Digits not found. Try entering actual numbers!",
    "My math teacher warned me about people like you. Numbers only, please!",
    "Oops! Looks like your keyboard accidentally spilled some alphabet soup.",
    "If I had a dollar for every letter you typed, I'd have zero dollars. Use digits!"
]


def greetings():
    return """Welcome to "Guess the Number"!

To start, pick your upper limit N, and I'll generate a secret number between 1 and N.
Your goal is to figure out what it is in as few tries as possible.
Just type in your guess, and after every attempt, I'll tell you if the secret number is higher or lower than your pick.
Keep guessing until you hit the mark and claim your victory!"""


def is_valid_limit(upper_limit):
    return upper_limit.isdigit() and int(upper_limit) > 0


def is_valid_guess(guess, upper_limit):
    return guess.isdigit() and 1 <= int(guess) <= int(upper_limit)


def one_more_time(again):
    while again not in ("yes", "no"):
        print("You are supposed to enter just 'yes' or 'no'")
        again = input("Do you want to play again?: yes/no: ")

    return again


print(greetings())


while True:
    limit_input = input("\nEnter upper limit N: ")
    while not is_valid_limit(limit_input):
        print("\nInvalid imput! Please enter a positive number.")
        limit_input = input("\nTry again.Enter upper limit N: ")

    upper_limit = int(limit_input)
    secret_number = random.randint(1, upper_limit)
    attempts_counter = 0

    while True:
        user_guess = input(f"\nGuess a number between 1 and {upper_limit}: ")
        if not is_valid_guess(user_guess, upper_limit):
            print(random.choice(ANSWERS))
            continue

        guess = int(user_guess)

        if guess < secret_number:
            print("\nToo low! Try again")
            attempts_counter += 1

        elif guess > secret_number:
            print("\nToo high! Try again")
            attempts_counter += 1

        else:
            print("\nYou won! Congratulations!")
            print(f"\nIt took you {attempts_counter} attempts to guess the secret number")

            attempts_counter += 1

            again = input("\nWanna play one more time? Enter 'yes' or 'no':  ")
            if one_more_time(again) == "yes":
                break
            else:
                print("\nThank you for the game, see you!")

                sys.exit()


