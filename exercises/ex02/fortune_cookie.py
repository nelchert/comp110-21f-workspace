"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730229567"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...

fortune: int = int(randint(1,100))

print("Your fortune cookie says...")

if fortune < 25:
    print("Watch out for snakes!")
else:
    if fortune < 50:
        print("True love is headed your way.")
    else:
        if fortune <= 75:
            print("Someone is keeping a secret from you.")
        else:
            print("Seven years of good luck are in your future.")

print("Now, go and spread positive vibes!")