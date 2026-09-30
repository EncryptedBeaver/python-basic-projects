ENG_LOWER_ALPHABET = "abcdefghijklmnopqrstuvwxyz"
ENG_UPPER_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
RUS_LOWER_ALPHABET = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
RUS_UPPER_ALPHABET = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


# Prompt the user to choose between 'encode' or 'decode' mode.
def ask_mode(prompt):
    user_answer = input(prompt).lower().strip()
    while user_answer not in ("decode", "encode"):
        print("Please enter only 'decode' or 'encode'")
        user_answer = input(prompt).lower().strip()
    return user_answer == "decode"


# Prompt the user to select the target language ('en' or 'ru').
def choose_language(prompt):
    user_answer = input(prompt).lower().strip()
    while user_answer not in ("en", "ru"):
        print("I don't understand your answer: please try again")
        user_answer = input(prompt).lower().strip()
    return user_answer


# Prompt for and validate an integer input for the shift step.
def check_num(prompt):
    user_num = input(prompt)
    while not user_num.isdigit():
        print("Please enter integer > 0")
        user_num = input(prompt)
    return int(user_num)


# Encrypt or decrypt text using the Caesar cipher algorithm.
def shifted_text(mode, language, text, rot):
    result_text = ""

    if language == "ru":
        lower_alph, upper_alph = RUS_LOWER_ALPHABET, RUS_UPPER_ALPHABET
    else:
        lower_alph, upper_alph = ENG_LOWER_ALPHABET, ENG_UPPER_ALPHABET

    if mode:
        rot = -rot

    for char in text:
        if char.isupper():
            idx = upper_alph.find(char)
            new_idx = (idx + rot) % len(upper_alph)
            result_text += upper_alph[new_idx]
        elif char.islower():
            idx = lower_alph.find(char)
            new_idx = (idx + rot) % len(lower_alph)
            result_text += lower_alph[new_idx]
        else:
            result_text += char

    return result_text


# Main Execution
mode = ask_mode("What do you want to do? ('encode' / 'decode'): ")
language = choose_language("Which language? ('en' / 'ru'): ")
shift = check_num("How many symbols to shift?: ")
user_text = input("Enter your text: ")

result = shifted_text(mode, language, user_text, shift)

print(result)
