import random

with open("words.txt") as file:
    word_string = file.read()
    word_list = word_string.split("\n")


def sort_by_difficulty(x=word_list):
    ycw_easy = [word for word in word_list if len(word) < 4]
    easy = [word for word in word_list if 3 < len(word) < 7]
    normal = [word for word in word_list if 6 < len(word) < 9]
    hard = [word for word in word_list if 8 < len(word)]
    return ycw_easy, easy, normal, hard


def pick_a_word(difficulty):
    return difficulty[random.randint(0, len(difficulty)-1)]


def game_setup():
    difficulty = input(
        "Please select your difficulty (ycw_easy, easy, normal, or hard): "
        )
    ycw_easy, easy, normal, hard = sort_by_difficulty()
    picked_word = pick_a_word(difficulty)
    return picked_word


def display_word(word, letters):
    guessed_list = []
    for letter in word:
        if letter in letters:
            guessed_list.append(letter)
        else:
            guessed_list.append('_')
    print(' '.join(guessed_list))



def run_game():
    mystery_word = "lamb"
    guesses_left = 8
    incorrect_guesses = []
    correct_guesses = []
    display_word(mystery_word, correct_guesses)
    if len(incorrect_guesses) > 0:
        print(f"Letter Graveyard: {', '.join(incorrect_guesses)}")
    print(f"You have {guesses_left} guesses left.")


run_game()
