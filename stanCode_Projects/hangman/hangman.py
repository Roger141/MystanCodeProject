"""
File: hangman.py
Name:Roger141
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    correct,wrong,win,game over
    """
    answer = random_word()
    answer = answer.upper()
    dashed = '-' * len(answer)
    lives = 7

    while True:
        print("The word looks like:"+ str(dashed))
        print("You have " + str(lives) + " wrong guesses left.")

        guess = input("Your guess: ")
        guess = guess.upper()
        # check Illegal format
        if len(guess) != 1 or not guess.isalpha():
            print("Illegal format.")

        ch = guess
        #correct
        if ch in answer:
            print("You are correct!")
            dashed = update_dashed(answer, dashed, ch)

            #win
            if dashed == answer:
                print("You win!!")
                print("The answer is:", answer)
                break

        # wrong
        else:
            print("There is no", ch + "'s in the word.")
            lives -= 1

            # game over
            if lives == 0:
                print("You are completely hung :(")
                print("The answer is:", answer)
                break


def update_dashed(answer, dashed, ch):
    """
    assign the correct guess
    """
    new_dashed = ''
    for i in range(len(answer)):
        if answer[i] == ch:
            new_dashed += ch
        else:
            new_dashed += dashed[i]
    return new_dashed


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
