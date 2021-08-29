"""COMP110 EXO1: numeric operators."""

__author__ = "730229567"

left: int = int(input("Left-hand side: "))
right: int = int(input("Right-hand side: "))
exponentation: int = left ** right
division: int = left / right
integer_division: int = left // right
remainder: int = left % right
print(str(left) + " ** " + str(right) + " is " + str(exponentation))
print(str(left) + " / " + str(right) + " is " + str(division))
print(str(left) + " // " + str(right) + " is " + str(integer_division))
print(str(left) + " % " + str(right) + " is " + str(remainder))