# Modify the program below to use a while loop to
# allow as many guesses as necessary.
#
# The program should let the player know whether to
# guess higher or lower, and should print a message
# when the guess is correct. A correct guess will
# terminate the program.
#
# As an optional extra, allow the player to quit by entering
# 0 (zero) for their guess.

import random

highest = 1000
answer = random.randint(1, highest)
game = True

while game:
    print("Select a number between 1 and {}\nSelect 0 to quit.".format(highest))
    guess = int(input())
    if guess == 0:
        game = False
        print("See you next time!")
    elif guess > answer:
        print("Too high! Go lower")
    elif guess < answer:
        print("Too low! Go higher!")
    elif guess == answer:
        game = False
        print("You got it! The number was {}\nSee you next time!".format(answer))

