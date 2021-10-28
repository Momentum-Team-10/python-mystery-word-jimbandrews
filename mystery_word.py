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


def display_word(word, letters=[]):
    guessed_list = []
    for letter in word:
        if letter in letters:
            guessed_list.append(letter)
        else:
            guessed_list.append('_')
    print(' '.join(guessed_list))


def start_game(mystery_word, correct):
    print("The Mystery Word has been selected!")



def run_game():
    mystery_word = "lamb"
    guesses_left = 8
    incorrect_guesses = []
    correct_guesses = []
    game_completed = False
    print("Welcome to the Mystery Word Game!")

    while game_completed == False:
        display_word(mystery_word, correct_guesses)
        if len(incorrect_guesses) > 0:
            print(f"Letter Graveyard: {', '.join(incorrect_guesses)}")
        print(f"You have {guesses_left} guesses left.")
        user_guess = input("Please guess a letter: ")
        if len(user_guess) > 1:
            print("Please guess one letter at a time.")
        elif user_guess == " ":
            print("Please guess a letter of the alphabet.")
        elif user_guess == "":
            print("Please guess a letter of the alphabet.")
        elif user_guess in incorrect_guesses or correct_guesses:
            print("You have already guessed that letter. Please try again.")
        else:
            if user_guess not in mystery_word:
                print("Sorry, that guess was incorrect.")
                incorrect_guesses.append(user_guess)
                guesses_left -= 1
            else:
                print("That's correct!")
                correct_guesses.append(user_guess)
        




run_game()
