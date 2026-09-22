import random

# Global variables
DIGITS = "0123456789"
LOWERCASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
PUNCTUATION = "!#$%&*+-=?@^"
SPECIAL_SYMBOLS = "il1Lo0O?"


# To check if user's input is digit
def ask_number(prompt):
    user_input = input(prompt).strip()
    while not user_input.isdigit() or int(user_input) < 1:
        print("Please enter integer: ")
        user_input = input(prompt).strip()
    return int(user_input)


# Make sure the user answer is 'yes' or 'no'
def ask_question(question_text):
    user_answer = input(question_text).lower().strip()
    while user_answer not in ("yes", "no"):
        print("Please enter only 'yes' or 'no': ")
        user_answer = input(question_text).lower().strip()
    return user_answer == "yes"


# What user wants to include in his password
def include_in_password():
    chars = ""

    if ask_question("Do you want digits in the password? (yes/no): "):
        chars += DIGITS

    if ask_question("Do you want upper latters in the password? (yes/no): "):
        chars += UPPERCASE_LETTERS

    if ask_question("Do you want lower latters in the password? (yes/no): "):
        chars += LOWERCASE_LETTERS

    if ask_question("Do you want symbols like (il1Lo0O?) in the password? (yes/no): "):
        chars += SPECIAL_SYMBOLS

    return chars


# Generate random passwords
def generate_password(length, chars, count):

    for _ in range(count):
        password_symbols = random.choices(chars, k=length)
        final_password = "".join(password_symbols)
        print(final_password)


# Ask a user how many passwords he wants to generate and how long they should be
password_count = ask_number("How many passwords do you want to generate?: ")
passwords_length = ask_number("How many symbols do you want in the password?: ")

# Symbols for passwords
chars = include_in_password()

# Start
if not chars:
    print("Error: you must create at lease one character set!")
else:
    generate_password(passwords_length, chars, password_count)
