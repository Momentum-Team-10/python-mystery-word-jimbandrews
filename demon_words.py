from itertools import combinations
import random


def build_word_list(length, word_list):
    '''
    parameters: chosen word length and a list of words
    returns: list of words of the length given
    '''
    return [word.upper() for word in word_list if len(word) == length]


def build_permutations(indices):
    '''
    parameter: a list of indices of blank spaces in the currently guessed word
    returns: a list of tuples, each containing a permutation of the indices
    '''
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
    '''
    paramter: a list of permutations (as tuples) of the blank space industries,
    the guessed word as a list, and the guessed letter
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
    '''
    parameters: string of letters and blanks (permutation), a string of all
        letters (word within mystery list)
    returns: word from mystery list with blank spaces in the same place as
        the permutation
    '''
    word = word.upper()
    listed_word = list(word)
    for tuple in enumerate(listed_word):
        index = tuple[0]
        if blanked[index] == '_':
            listed_word.pop(index)
            listed_word.insert(index, '_')
    return ''.join(listed_word)


def counting_guess(guess, word):
    occurrences = 0
    for letter in word:
        if letter == guess:
            occurrences += 1
    return occurrences


def fill_families_dict(families_dict, words_list, guessed_word, guess):
    '''
    parameters: dictionary with permutations as keys and empty lists as values,
        a list of words, the currently guessed word as a list
    returns: dictionary with lists filled with words whose letters match those
        of the corresponding key
    '''
    matched_words = []
    occurrences_dict = {}
    list_copy = words_list.copy()
    permutations = list(families_dict.keys())
    for perm in permutations:
        for word in words_list:
            if word in matched_words:
                continue
            elif guess not in word:
                continue
            elif word in occurrences_dict.keys():
                word_count = occurrences_dict[word]
            else:
                word_count = counting_guess(guess, word)
            blanked = convert_word(perm, word)
            blanked_count = counting_guess(guess, blanked)
            if word_count == blanked_count:
                families_dict[perm].append(word)
                matched_words.append(word)
                list_copy.remove(word)
            else:
                occurrences_dict[word] = word_count
    families_dict[''.join(guessed_word)] = list_copy
    breakpoint()
    return families_dict


def find_new_list_and_word(current_word, new_guess, words_list):
    '''
    parameters: currently guessed word as a list, the new guess from the
        player, and a list of words
    returns: new currently guessed word and word list
    '''
    blanks = build_blank_indices(current_word)
    index_permutations = build_permutations(blanks)
    families_dict = build_families_dict(
        index_permutations, current_word, new_guess
    )
    filled_families = fill_families_dict(
        families_dict, words_list, current_word, new_guess
    )
    max_list_key = ''.join(current_word)
    for permutation in filled_families.keys():
        permutation_list = filled_families[permutation]
        if len(permutation_list) > len(filled_families[max_list_key]):
            max_list_key = permutation
    new_current_word = list(max_list_key)
    new_word_list = filled_families[max_list_key]
    return new_current_word, new_word_list


def game_display(guessed_word, guessed_letters, guesses_left):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(" ".join(guessed_word))
    if len(guessed_letters) > 0:
        print(f"Letter Graveyard: {', '.join(guessed_letters)}")
    print(f"You have {guesses_left} guesses left.")


def choose_difficulty():
    '''
    returns: player-chosen length of mystery word
    '''
    print()
    word_length = input("How long would you like the mystery word to be? ")
    while word_length.isnumeric() is False:
        print("Sorry, that is not a valid number.")
        word_length = input("Please enter a positive whole number: ")
    return int(word_length)


def is_game_complete(guesses_left, guessed_word, word_list, letter_list):
    '''
    parameters: number of guesses left, currently guessed word, and list of
        words
    returns: boolean of if the game is completed
    '''
    if guesses_left == 0:
        game_completed = True
        print("Oh no! You don't have any more guesses left!")
        correct_word = word_list[random.randrange(0, len(word_list))]
        print(f"The word we were looking for was {correct_word}")
    elif '_' not in guessed_word:
        game_completed = True
        print("Congrats! you've guessed the Mystery Word!")
        print(f"It took you {len(letter_list)} guesses to win.")
    else:
        game_completed = False
    return game_completed


def is_new_game():
    '''
    returns: boolean of if a new game should start
    '''
    yes = ['YES', 'Y', 'YE', 'YS']
    no = ['NO', 'N']
    play_again = input("Would you like to play again? ").upper()
    while play_again not in yes and play_again not in no:
        play_again = input("Please answer 'Yes' or 'No': ")
    if play_again in yes:
        new_game = True
    if play_again in no:
        new_game = False
    return new_game


def game_start():
    '''
    returns: boolean indicating whether to start the game
    '''
    print("WELCOME!\n")
    print(
        "Is the regular Mystery Word game too simple for you?",
        "Are you looking for a bigger challenge?",
        "Then step right up, this is the game for you!",
        "But be warned,",
        "this game is harder than The Lion King on the Sega Genesis\n"
    )
    response = input("Are you sure you want to play?\n").upper()
    yes = ['YES', 'Y', 'YE', 'YS']
    no = ['NO', 'N']
    while response not in yes and response not in no:
        response = input("What was that? Come now, speak up. ").upper()
    if response in yes:
        return True
    elif response in no:
        return False


def run_game():
    new_game = game_start()

    while new_game is True:
        with open("words.txt") as file:
            word_string = file.read()
            main_word_list = word_string.split("\n")

        mystery_length = choose_difficulty()
        guessed_word = list(mystery_length * '_')
        mystery_list = build_word_list(mystery_length, main_word_list)
        game_completed = False
        guessed_letters = []
        guesses_left = 24

        while game_completed is False:
            game_display(guessed_word, guessed_letters, guesses_left)
            user_guess = input("Please guess a letter from the alphabet: ")

            while len(user_guess) != 1:
                user_guess = input("Please guess one letter at a time: ")
            while user_guess.isalpha() is False:
                user_guess = input("That is not a letter. Please try again: ")
            user_guess = user_guess.upper()
            while user_guess in guessed_letters:
                user_guess = input(
                    "You have already guessed that letter. Please try again: "
                ).upper()

            guessed_letters.append(user_guess)
            guessed_word, mystery_list = find_new_list_and_word(
                guessed_word, user_guess, mystery_list
            )
            guesses_left -= 1

            game_completed = is_game_complete(
                guesses_left, guessed_word, mystery_list, guessed_letters
            )
        new_game = is_new_game()


run_game()
