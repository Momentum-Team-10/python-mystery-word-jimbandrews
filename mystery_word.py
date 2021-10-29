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
    print("Welcome to the Mystery Word Game!")
    difficulty = input(
        "Please select your difficulty (ycw_easy, easy, normal, or hard): "
        )
    ycw_easy, easy, normal, hard = sort_by_difficulty()
    picked_word = pick_a_word(difficulty)
    return picked_word


def game_display(word, correct, incorrect, guesses_left):
    guessed_list = []
    for letter in word:
        if letter in correct:
            guessed_list.append(letter)
        else:
            guessed_list.append('_')
    print(' '.join(guessed_list))
    if len(incorrect) > 0:
        print(f"Letter Graveyard: {', '.join(incorrect)}")
    print(f"You have {guesses_left} guesses left.")
    return guessed_list


def start_game(mystery_word, correct):
    print("The Mystery Word has been selected!")


def check_guess(mystery_word, user_guess, guesses_left, incorrect, correct):
    if len(user_guess) > 1:
        print("Please guess one letter at a time.")
    elif user_guess == " ":
        print("Please guess a letter of the alphabet.")
    elif user_guess == "":
        print("Please guess a letter of the alphabet.")
    elif user_guess in incorrect or user_guess in correct:
        print("You have already guessed that letter. Please try again.")
    elif user_guess not in mystery_word:
        print("Sorry, that guess was incorrect.")
        incorrect.append(user_guess)
        guesses_left -= 1
    else:
        print("That's correct!")
        correct.append(user_guess)
    return guesses_left, incorrect, correct


def run_game():
    mystery_word = "LAMB"
    guesses_left = 8
    incorrect_guesses = []
    correct_guesses = []
    game_completed = False
    print("Welcome to the Mystery Word Game!")

    while game_completed is False:
        guessed_word = game_display(
            mystery_word, correct_guesses, incorrect_guesses, guesses_left
            )
        user_guess = input("Please guess a letter: ").upper()
        guesses_left, incorrect_guesses, correct_guesses = check_guess(
            mystery_word, user_guess, guesses_left, incorrect_guesses,
            correct_guesses
        )
        if guesses_left == 0:
            print("Oh no! You've run out of guesses!")
            print(f"The Mystery Word was {mystery_word}")
            game_completed = True
        elif list(mystery_word) == guessed_word:
            print("Congrats! You guessed the mystery word!")
            print(
                f"It took you {len(incorrect_guesses)+len(correct_guesses)} guesses to win."
                )
            game_completed = True


run_game()
