import random

HANGMAN_ASCII_ART = ("""
     | |  | |
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |
                         |___/ 
animal quiz let's go!""")

PICTURE_1 = 'x-------x'
PICTURE_2 = """
x-------x
    |
    |
    |
    |
    |"""

PICTURE_3 = """
x-------x
    |       |
    |       0
    |
    |
    |"""

PICTURE_4 = """
x-------x
    |       |
    |       0
    |       |
    |
    |
"""

PICTURE_5 = """
x-------x
    |       |
    |       0
    |      /|\\
    |
    |
"""

PICTURE_6 = """
x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
"""

PICTURE_7 = """
x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
"""
HANGMAN_PHOTOS = [PICTURE_1, PICTURE_2, PICTURE_3, PICTURE_4, PICTURE_5, PICTURE_6, PICTURE_7]
MAX_MISTAKES = 7
MAX_MISTAKES_MESSAGE = f"max mistakes: {MAX_MISTAKES}"
SECRET_LETTER_SYMBOL = "_"


def check_win(secret_word, guessed_letters):
    """
    check if all the old letters are in the secret word and return true / false
    :param secret_word:
    :param guessed_letters:
    :return: True, False
    """
    return get_hidden_word(secret_word, guessed_letters) == secret_word


def get_hidden_word(secret_word, letters_guessed):
    """
    check if all the old letters are in the secret word and show them, else print '_' insted of the letter
    :param secret_word:
    :param letters_guessed:
    :return: (''.join(guessed_word))
    """
    guessed_word = ""
    for letter in secret_word:
        guessed_word += letter if letter in letters_guessed else SECRET_LETTER_SYMBOL
    return guessed_word


def get_user_input(prompt, guessed_letters):
    letter = input(prompt).lower()
    while not is_input_valid(letter, guessed_letters):
        print(f"Please make sure to enter one letter from the abc which isn't one of {guessed_letters}")
        letter = input(prompt).lower()
    return letter


def is_input_valid(letter_guessed, old_letters_guessed):
    """
     check if the guesser's letter is a valid input
    :param letter_guessed:
    :param old_letters_guessed:
    :return: True, False
    """
    return len(letter_guessed) == 1 and letter_guessed.isalpha() and letter_guessed not in old_letters_guessed


def choose_word(file_path):
    """
    choosing the word out of a file of animal names
    :param file_path:
    :return: the secret word
    """
    with open(file_path) as words_file:
        words = words_file.read().strip().split(", ")
    return random.choice(words)


def main():
    print(HANGMAN_ASCII_ART)
    print(MAX_MISTAKES_MESSAGE)

    secret_word = choose_word("./findme.txt")
    guessed_letters = []
    num_of_tries = 1

    while True:
        print(HANGMAN_PHOTOS[num_of_tries - 1])
        print(get_hidden_word(secret_word, guessed_letters))

        if num_of_tries == MAX_MISTAKES:
            print("you lose :(\nthe word was " + secret_word + " you can always win next time")
            break

        if check_win(secret_word, guessed_letters):
            print("you won!!!")
            break

        letter_guessed = get_user_input('choose a letter:', guessed_letters)
        guessed_letters.append(letter_guessed.lower())
        print(f"the letter you choose: {letter_guessed}")
        print(f"used letters: {guessed_letters}")

        if letter_guessed not in secret_word:
            num_of_tries += 1


if __name__ == "__main__":
    main()
