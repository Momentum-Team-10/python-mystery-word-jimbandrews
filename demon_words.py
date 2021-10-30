# from math import factorial
from itertools import permutations


with open("words.txt") as file:
    word_string = file.read()
    main_word_list = word_string.split("\n")


def build_word_list(length, word_list):
    return [word.lower() for word in word_list if len(word) == length]


# def build_mini_word_list(word_list, guessed_word):
#     return [word for word in word_list if list(word) == guessed_word]

# # returns the number of permutations for a specific number of letters
# # (letters_num) in a number of available spaces (total_spaces)
# def distinguishable_perm(letters_num, total_spaces):
#     spaces = total_spaces - letters_num
#     return factorial(total_spaces) / (
#         factorial(letters_num) * factorial(spaces)
#         )


# given a list of letters and spaces, returns a list of permutations
# each permutation is a tuple
def build_permutations(letters_list):
    perms = list(permutations(letters_list))
    no_repeat = []
    for tuple in perms:
        if tuple in no_repeat:
            continue
        else:
            no_repeat.append(tuple)
    return no_repeat


def create_perm_seeds(letter, blanks):
    perm_seeds = []
    for index in range(len(blanks)):
        blanks[index] = letter
        copy = blanks.copy()
        perm_seeds.append(copy)
    return perm_seeds


def set_passing_match_score(permutation):
    passing_score = 0
    for letter in permutation:
        if letter == '_':
            continue
        else:
            passing_score += 1
    return passing_score


def fill_permutations_dict(guessed_letter, current_word):
    current_blanks = current_word.copy()
    for letter in current_word:
        if letter != "_":
            current_blanks.remove(letter)
    all_permutations = {}
    permutation_seeds = create_perm_seeds(guessed_letter, current_word)
    for seed in permutation_seeds:
        perms = build_permutations(seed)
        for permutation in perms:
            all_permutations[tuple(permutation)] = []
    all_permutations[tuple(current_blanks)] = []
    return all_permutations


# types: string, list, list, dictionary
def find_new_mystery_list(
    guessed_letter, current_word, main_list, perm_dict
):
    matched_words = []
    all_permutations = fill_permutations_dict(guessed_letter, current_word)
    for permutation in all_permutations.keys():
        perm_list = list(permutation)
        for letter in perm_dict.keys():
            perm_list.insert(perm_dict[letter], letter)
        perm_string = "".join(perm_list).lower()
        passing_score = set_passing_match_score(perm_string)
        for word in main_list:
            if word in matched_words:
                continue
            match_score = 0
            for index in range(len(word)):
                if word[index] == perm_string[index]:
                    match_score += 1
            if match_score == passing_score:
                all_permutations[permutation].append(word)
                matched_words.append(word)
    all_perm_keys = list(all_permutations.keys())
    max_word_family = all_perm_keys[0]
    for permutation in all_perm_keys:
        if len(all_permutations[permutation]) > len(all_permutations[max_word_family]):
            max_word_family = permutation
    new_mystery_list = all_permutations[max_word_family]
    new_current_word = max_word_family
    return new_mystery_list, new_current_word


def run_game(word_list):
    new_game = True

    while new_game is True:
        # Temporary placeholder; will let player select word lenght later
        mystery_length = 4
        game_completed = False
        mystery_list = build_word_list(mystery_length, word_list)
        guessed_word = list(mystery_length * "_")
        permanent_letters = {}

        while game_completed is False:
            breakpoint()
            print(" ".join(guessed_word))
            user_guess = input("Please guess a letter from the alphabet: ")
            while user_guess.isalpha() is False:
                user_guess = input("That is not a letter. Please try again: ")
            user_guess = user_guess.upper()
            mystery_list, guessed_word_tuple = find_new_mystery_list(
                user_guess, guessed_word, mystery_list, permanent_letters
            )
            guessed_word = list(guessed_word_tuple)


run_game(main_word_list)
