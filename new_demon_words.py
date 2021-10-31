from itertools import combinations


def build_word_list(length, word_list):
    return [word.upper() for word in word_list if len(word) == length]


def build_permutations(indices):
    index_perms = []
    for length in range(1, len(indices)+1):
        perms_list = list(combinations(indices, length))
        index_perms.extend(perms_list)
    return index_perms


def build_blank_indices(word):
    '''
    parameter: the word as a list
    returns: a list of the indices of the blank spaces
    '''
    blank_indices = []
    for index in range(len(word)):
        if word[index] == '_':
            blank_indices.append(index)
    return blank_indices


def build_families_dict(index_perms, word, letter):
    # note: here, word is of type list
    '''
    paramter: a list of permutations of the blank space industries, the guessed
    word as a list, and the guessed letter
    returns: dictionary where the keys are all the permutations adding the
    letter to the blanks in the guessed word; and the values are empty lists
    '''
    word_families_dict = {}
    for tuple in index_perms:
        copy = word.copy()
        for index in tuple:
            copy[index] = letter
        word_families_dict["".join(copy)] = []
    return word_families_dict


def convert_word(blanked, word):
    word = word.upper()
    listed_word = list(word)
    for letter in listed_word:
        index = listed_word.index(letter)
        if blanked[index] == '_':
            listed_word.pop(index)
            listed_word.insert(index, '_')
    return ''.join(listed_word)


# need to fix a bug here; lines 74,75 only need to run if it is the first guess
def fill_families_dict(families_dict, words_list, guessed_word):
    matched_words = []
    list_copy = words_list.copy()
    for permutation in families_dict:
        for word in words_list:
            if word in matched_words:
                continue
            blanked = convert_word(permutation, word)
            if blanked == permutation:
                families_dict[permutation].append(word)
                matched_words.append(word)
                list_copy.remove(word)
    families_dict[''.join(guessed_word)] = list_copy
    return families_dict


def find_new_list_and_word(current_word, new_guess, words_list):
    blanks = build_blank_indices(current_word)
    index_permutations = build_permutations(blanks)
    families_dict = build_families_dict(
        index_permutations, current_word, new_guess
    )
    filled_families = fill_families_dict(families_dict, words_list, current_word)
    max_list_key = ''.join(current_word)
    for permutation in filled_families:
        if len(filled_families[permutation]) > len(filled_families[max_list_key]):
            max_list_key = permutation
    new_current_word = list(max_list_key)
    new_word_list = filled_families[max_list_key]
    return new_current_word, new_word_list


def game_display(guessed_word, guessed_letters):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(" ".join(guessed_word))
    if len(guessed_letters) > 0:
        print(f"Letter Graveyard: {', '.join(guessed_letters)}")


def choose_difficulty():
    word_length = input("How long would you like the mystery word to be? ")
    while word_length.isnumeric() is False:
        print("Sorry, that is not a valid number.")
        word_length = input("Please enter a positive whole number: ")
    return int(word_length)


# add in word_list as a parameter later
def run_game():
    new_game = True

    while new_game is True:
        # placeholders to get code to work
        # mystery_list = ['echo', 'heal', 'best', 'lazy']
        # guessed_word = ['_', '_', '_', '_']

        with open("words.txt") as file:
            word_string = file.read()
            main_word_list = word_string.split("\n")

        mystery_length = choose_difficulty()
        guessed_word = mystery_length * '_'
        mystery_list = build_word_list(mystery_length, main_word_list)
        breakpoint()
        game_completed = False
        guessed_letters = []

        while game_completed is False:
            game_display(guessed_word, guessed_letters)
            user_guess = input("Please guess a letter from the alphabet: ")
            while len(user_guess) != 1:
                user_guess = input("Please guess one letter at a time: ")
            while user_guess.isalpha() is False:
                user_guess = input("That is not a letter. Please try again: ")
            user_guess = user_guess.upper()
            while user_guess in guessed_letters:
                user_guess = input(
                    "You have already guessed that letter. Please try again: "
                )
            guessed_letters.append(user_guess)
            guessed_word, mystery_list = find_new_list_and_word(guessed_word, user_guess, mystery_list)


run_game()
