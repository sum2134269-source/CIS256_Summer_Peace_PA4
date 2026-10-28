
# Summer Peace
# CIS256 Fall 2026
# Programming Assignment 4

from guess_the_word import (
    WORDS,
    select_word,
    check_guess,
    display_word
)


# Test that the selected word is from the predefined list.
def test_select_word():
    for _ in range(20):
        assert select_word() in WORDS


# Test that a correct letter guess is recognized.
def test_correct_guess():
    guessed_letters = set()
    assert check_guess("python", "p", guessed_letters) is True
    assert "p" in guessed_letters


# Test that an incorrect letter guess is recognized.
def test_incorrect_guess():
    guessed_letters = set()
    assert check_guess("python", "z", guessed_letters) is False
    assert "z" in guessed_letters


# Test that all repeated letters are revealed.
def test_repeated_letters():
    guessed_letters = {"s"}
    assert display_word("success", guessed_letters) == "s _ _ _ _ s s"


# Test that letters can be guessed in any order.
def test_letters_any_order():
    guessed_letters = {"n", "p"}
    assert display_word("python", guessed_letters) == "p _ _ _ _ n"
