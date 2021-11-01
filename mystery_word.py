import random

with open("words.txt") as file:
    word_string = file.read()
    word_list = word_string.split("\n")


def run_game():
    new_game = True

    while new_game is True:

        print("Welcome to the Mystery Word Game!")
        mystery_word = game_setup()
        guesses_left = 8
        incorrect_list = []
        correct_list = []
        game_completed = False

        while game_completed is False:
            game_display(
                mystery_word, correct_list, incorrect_list, guesses_left
                )
            user_guess = input("Please guess a letter: ").upper()
            guesses_left, incorrect_list, correct_list = check_guess(
                mystery_word, user_guess, guesses_left, incorrect_list,
                correct_list
            )
            guessed_list = guessed_word(mystery_word, correct_list)
            if guesses_left == 0:
                print("Oh no! You've run out of guesses!")
                print(f"The Mystery Word was {mystery_word}")
                game_completed = True
            elif list(mystery_word) == guessed_list:
                total_guesses = len(incorrect_list)+len(correct_list)
                print(' '.join(guessed_list))
                print("Congrats! You guessed the mystery word!")
                print(
                    f"It took you {total_guesses} guesses to win."
                    )
                game_completed = True

        new_game = end_game()


def game_setup():
    difficulties = ["ycw", "easy", "normal", "hard"]
    print("Welcome to the Mystery Word Game!")
    difficulty = input(
        "Please select your difficulty (ycw, easy, normal, or hard): "
        ).lower()
    while difficulty not in difficulties:
        difficulty = input(
            "Please choose ycw, easy, normal, or hard as a difficulty: "
        ).lower()
    difficulty_list = build_difficulty_list(difficulty, word_list)
    picked_word = pick_a_word(difficulty_list)
    return picked_word.upper()


def build_difficulty_list(difficulty, word_list):
    if difficulty == "ycw":
        diff_list = [word for word in word_list if len(word) < 4]
    elif difficulty == "easy":
        diff_list = [word for word in word_list if 3 < len(word) < 7]
    elif difficulty == "normal":
        diff_list = [word for word in word_list if 6 < len(word) < 9]
    elif difficulty == "hard":
        diff_list = [word for word in word_list if 8 < len(word)]
    return diff_list


def pick_a_word(difficulty_list):
    return difficulty_list[random.randint(0, len(difficulty_list)-1)]


def game_display(word, correct, incorrect, guesses_left):
    guessed_list = guessed_word(word, correct)
    print(' '.join(guessed_list))
    if len(incorrect) > 0:
        print(f"Letter Graveyard: {', '.join(incorrect)}")
    print(f"You have {guesses_left} guesses left.")


def guessed_word(word, correct):
    guessed_list = []
    for letter in word:
        if letter in correct:
            guessed_list.append(letter)
        else:
            guessed_list.append('_')
    return guessed_list


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


def end_game():
    play_again = input("Would you like to play again? (Yes/No) ").lower()
    while play_again != "yes" and play_again != "no":
        play_again = input("Please enter 'Yes' or 'No'.").lower()
    if play_again == "yes":
        new_game = True
    elif play_again == "no":
        new_game = False
    return new_game


run_game()
