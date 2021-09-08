"""Repeating a beat in a loop."""

__author__ = "730229567"

beat: str = str(input("What beat do you want to repeat? "))
s: int = int(input("How many times do you want to repeat it? "))
x = 0
p = str("")

while s > 0:
    if s == x:
        p = p , beat
    else:
        x = x + 1
s += 1

print(p)