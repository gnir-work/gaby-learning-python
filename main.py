def opening_of_the_game():
    HANGMAN_ASCII_ART = ("""
     | |  | |
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |
                         |___/ 
animal quiz let's go!""")
    MAX_TRIES = "max mistakes: 6"
    print(HANGMAN_ASCII_ART)
    print(MAX_TRIES)


opening_of_the_game()


def print_hangman(num_of_tries):
    """
    the picture state of the game based on the num of tries
    :param num_of_tries:
    :return: HANGMAN_PHOTOS[num_of_tries]
    """
    picture_1 = 'x-------x'
    picture_2 = """
    x-------x
        |
        |
        |
        |
        |"""

    picture_3 = """
    x-------x
        |       |
        |       0
        |
        |
        |"""

    picture_4 = """
    x-------x
        |       |
        |       0
        |       |
        |
        |
    """

    picture_5 = """
    x-------x
        |       |
        |       0
        |      /|\\
        |
        |
    """

    picture_6 = """
    x-------x
        |       |
        |       0
        |      /|\\
        |      /
        |
    """

    picture_7 = """
    x-------x
        |       |
        |       0
        |      /|\\
        |      / \\
        |
    """
    HANGMAN_PHOTOS = {1: picture_1, 2: picture_2, 3: picture_3, 4: picture_4, 5: picture_5, 6: picture_6, 7: picture_7}
    return HANGMAN_PHOTOS[num_of_tries]


def check_win(secret_word, old_letters_guessed):
    """
    check if all the old letters are in the secret word and return true / false
    :param secret_word:
    :param old_letters_guessed:
    :return: True, False
    """
    guessed_word = []
    for i in range(len(secret_word)):
        secret_word_list = list(secret_word)
        if secret_word_list[i] in old_letters_guessed:
            guessed_word.append(secret_word_list[i])
        else:
            guessed_word.append('_')
        while secret_word_list[i] == secret_word_list[-1]:
            if guessed_word == secret_word_list:
                return True
            else:
                return False


def show_hidden_word(secret_word, old_letters_guessed):
    """
    check if all the old letters are in the secret word and show them, else print '_' insted of the letter
    :param secret_word:
    :param old_letters_guessed:
    :return: (''.join(guessed_word))
    """
    guessed_word = []
    for i in range(len(secret_word)):
        secret_word_list = list(secret_word)
        if secret_word_list[i] in old_letters_guessed:
            guessed_word.append(secret_word_list[i])
        else:
            guessed_word.append('_')
    return (''.join(guessed_word))


def check_valid_input(letter_guessed, old_letters_guessed):
    """
     check if the guesser's letter is a valid input
    :param letter_guessed:
    :param old_letters_guessed:
    :return: True, False
    """
    if len(letter_guessed) == 1 and letter_guessed.isalpha() and letter_guessed.lower() not in old_letters_guessed:
        return True
    else:
        return False


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    show the progress of guessing letters based on "check valid input" return + adding the letter to old_letter_guessed
    :param letter_guessed:
    :param old_letters_guessed:
    :return: none
    """
    if (bool(check_valid_input(letter_guessed, old_letters_guessed))):
        old_letters_guessed.append(letter_guessed.lower())
        print("the letter you choose: " + letter_guessed.lower())
        print('used letters: ', old_letters_guessed)
    else:
        print('X', '\n' + "->".join(old_letters_guessed), '\nFalse')


def choose_word(file_path, index):
    """
    choosing the word out of a file of animal names
    :param file_path:
    :param index:
    :return: the secret word
    """
    read_file = file_path.read()
    splited_words = read_file.split(", ")
    list_of_words = []
    for word in splited_words:
        if word in list_of_words:
            continue
        list_of_words.append(word)
    num_of_words = len(list_of_words)
    the_whole_list_of_words = len(splited_words)
    if index > the_whole_list_of_words:
        index = index % the_whole_list_of_words
    index = (splited_words[index - 1])
    secret_word = index
    the_tuple = "there are %d in the list, you choose the word:" % (num_of_words) + index  # for mission in files
    file_path.close()
    return secret_word


import random


def main():
    f = open(r'findme.txt', 'r')
    secret_word = choose_word(f, random.randint(0, 50))
    old_letters_guessed = []
    num_of_tries = 1
    while num_of_tries < 7:
        print(print_hangman(num_of_tries))
        print(show_hidden_word(secret_word, old_letters_guessed))
        letter_guessed = input('choose a letter:')
        bool = check_valid_input(letter_guessed, old_letters_guessed)
        try_update_letter_guessed(letter_guessed, old_letters_guessed)
        if bool == False:
            continue
        if check_win(secret_word, old_letters_guessed) == True:
            print("you won")
            print(show_hidden_word(secret_word, old_letters_guessed))
            break
        if letter_guessed not in secret_word:
            num_of_tries += 1
    if num_of_tries == 7:
        print(print_hangman(num_of_tries))
        print("you lose :(\nthe word was " + secret_word + " you can always win next time")


if __name__ == "__main__":
    main()

