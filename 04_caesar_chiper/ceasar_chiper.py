ENG_LOWER_ALPHABET = "abcdefghijklmnopqrstuvwxyz"
ENG_UPPER_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
RUS_LOWER_ALPHABET = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
RUS_UPPER_ALPHABET = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


# Ask user what he wants to do: 'decode' = True or 'encode' = False the line
def ask_mode(prompt):
    user_answer = input(prompt).lower().strip()
    while user_answer not in ("decode", "encode"):
        print("Please enter only 'decode' or 'encode'")
        user_answer = input(prompt).lower().strip()
    return user_answer == "decode"


# Ask user to choose language (EN or RU)
def choose_language(prompt):
    user_answer = input(prompt).lower().strip()
    while user_answer not in ("en", "ru"):
        print("I don't understand your answer: please try again")
        user_answer = input(prompt).lower().strip()
    return user_answer


# Check if the user entered integer
def check_num(n_shift):
    user_num = input(n_shift)
    while not user_num.isdigit():
        print("Please enter integer > 0")
        user_num = input(n_shift)

    return int(user_num)


# Main function
def shifted_text(text, rot, language, mode):

    rusult_text = ""

    # For Russian text
    if language == "ru":
        # If user wants to encode the text
        if not mode:
            for char in text:
                if char.isupper():
                    idx = RUS_UPPER_ALPHABET.find(char)
                    new_idx = (idx + rot) % len(RUS_UPPER_ALPHABET)
                    rusult_text += RUS_UPPER_ALPHABET[new_idx]

                elif char.islower():
                    idx = RUS_LOWER_ALPHABET.find(char)
                    new_idx = (idx + rot) % len(RUS_LOWER_ALPHABET)
                    rusult_text += RUS_LOWER_ALPHABET[new_idx]

                else:
                    rusult_text += char

        # If user wants to decode the text
        else:
            for char in text:
                if char.isupper():
                    idx = RUS_UPPER_ALPHABET.find(char)
                    new_idx = (idx - rot) % len(RUS_UPPER_ALPHABET)
                    rusult_text += RUS_UPPER_ALPHABET[new_idx]

                elif char.islower():
                    idx = RUS_LOWER_ALPHABET.find(char)
                    new_idx = (idx - rot) % len(RUS_LOWER_ALPHABET)
                    rusult_text += RUS_LOWER_ALPHABET[new_idx]

                else:
                    rusult_text += char

    # For English text
    if language == "en":
        # If user wants to encode the text
        if not mode:
            for char in text:
                if char.isupper():
                    idx = ENG_UPPER_ALPHABET.find(char)
                    new_idx = (idx + rot) % len(ENG_UPPER_ALPHABET)
                    rusult_text += ENG_UPPER_ALPHABET[new_idx]

                elif char.islower():
                    idx = ENG_LOWER_ALPHABET.find(char)
                    new_idx = (idx + rot) % len(ENG_LOWER_ALPHABET)
                    rusult_text += ENG_LOWER_ALPHABET[new_idx]

                else:
                    rusult_text += char

        # If user wants to decode the text
        else:
            for char in text:
                if char.isupper():
                    idx = ENG_UPPER_ALPHABET.find(char)
                    new_idx = (idx - rot) % len(ENG_UPPER_ALPHABET)
                    rusult_text += ENG_UPPER_ALPHABET[new_idx]

                elif char.islower():
                    idx = ENG_LOWER_ALPHABET.find(char)
                    new_idx = (idx - rot) % len(ENG_LOWER_ALPHABET)
                    rusult_text += ENG_LOWER_ALPHABET[new_idx]

                else:
                    rusult_text += char

    return rusult_text


n_shift = "How many symbols do you want to shift to the right? "
which_language = "Which language do you prefer? Enter: en/ru "
which_mode = "What do you want to do with your text: Enter: 'encode' or 'decode' ? "
user_text = input("Input the text you want to 'encode' or 'decode': ")

print(
    shifted_text(
        user_text,
        check_num(n_shift),
        choose_language(which_language),
        ask_mode(which_mode),
    )
)
