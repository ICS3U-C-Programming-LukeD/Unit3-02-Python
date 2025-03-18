#!/usr/bin/env python3

# Created By: Luke
# Date: March 17, 2025
# Asks user to guess the right number

from consts import NUMBER

import math  # Module library import


def main():
    print("Guess the right number!")
    # Intro message
    user_number = int(input(("Enter number: ")))
    # Asks user for guessed number
    print()
    if user_number == NUMBER:
        print("You Guessed Right!")
    if user_number != NUMBER:
        print("You Guessed Wrong, Try Again!")
    # Displays message depending on the number guessed


if __name__ == "__main__":
    main()
