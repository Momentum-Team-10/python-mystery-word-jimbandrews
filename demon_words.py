# from math import factorial


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


def run_game(word_list):
    new_game = True

    while new_game is True:
        # Temporary placeholder; will let player select word lenght later
        mystery_length = 4
        game_completed = False
        mystery_list = build_word_list(mystery_length, word_list)
        breakpoint()
        guessed_word = list(mystery_length * "_")

        while game_completed is False:
            user_guess = input(
                "Please guess a letter from the alphabet: "
                ).upper()
            

run_game(main_word_list)
