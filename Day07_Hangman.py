import random
import os

word = "python".lower()

def good_word(solution, target):
    return solution == target

def hangman():
    nb_tentatives = 0
    max_tentatives = 12
    display_word = "_" * len(word)

    while nb_tentatives < max_tentatives:
        letter = [input("Veuillez entrer une lettre : ").lower()]

        new_display, increment = good_letter(letter, display_word)

        if increment:
            nb_tentatives += 1

        display_word = new_display
        print(display_word, f"nombre de tentatives {nb_tentatives}/{max_tentatives}")

        if nb_tentatives == max_tentatives:
            print("Game over")
            break

        if new_display == word:
            print(f"Mot trouvé ! avec un score de {nb_tentatives}/{max_tentatives}")


def good_letter(letter, display_word):
    new_display = ""
    found = False
    for i, char in enumerate(word):
        if char == letter:
            new_display += letter
            found = True
        else:
            new_display += display_word[i]
    return new_display, not found


# PAS FINI