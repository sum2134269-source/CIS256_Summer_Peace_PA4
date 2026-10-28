
# Summer Peace
# CIS256 Fall 2026
# Programming Assignment 4

import random

# Words that can be selected for the game.
WORDS = ["python", "school", "success", "coding", "career"]


def select_word():
    # Randomly select a word.
    return random.choice(WORDS)


def check_guess(word, letter, guessed_letters):
    guessed_letters.add(letter)
    return letter in word


def display_word(word, guessed_letters):
    # Reveal all correctly guessed letters.
    return " ".join(
        letter if letter in guessed_letters else "_"
        for letter in word
    )


def play_game():
    word = select_word()
    guessed_letters = set()
    # Players get six incorrect guesses before the game ends.
    attempts = 6

    print("Welcome to Summer's Word Guessing Game!")

    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))
        print("Attempts remaining:", attempts)

        guess = input("Guess one letter: ").lower().strip()

        # Check for valid input.
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter one letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        if check_guess(word, guess, guessed_letters):
            print("Correct guess!")
        else:
            attempts -= 1
            print("Incorrect guess!")

        # Check if the entire word has been guessed.
        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed:", word)
            return

    print("Game over! The word was:", word)


# Only start the game when run directly.
if __name__ == "__main__":
    play_game()
