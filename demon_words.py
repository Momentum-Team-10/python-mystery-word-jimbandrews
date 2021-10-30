# from math import factorial
from itertools import permutations


with open("words.txt") as file:
    word_string = file.read()
    main_word_list = word_string.split("\n")


def build_word_list(length, word_list):
    return [word for word in word_list if len(word) == length]


def build_mini_word_list(word_list, guessed_word):
    return [word for word in word_list if list(word) == guessed_word]

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
    for tuple in no_repeat:
        list(tuple)
    return no_repeat


def find_new_mystery_list(guessed_letter, current_word, perm_dict, ):



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
            user_guess = input(
                "Please guess a letter from the alphabet: "
                ).upper()
            

run_game(main_word_list)
