"""COMP110 EXO1: relational operators."""

__author__ = "730229567"

left: int = int(input("Left-hand side: "))
right: int = int(input("Right-hand side: "))
less_than: bool = left < right
at_least: bool = left >= right
equal: bool = left == right
not_equal: bool = left != right
print(str(left) + " < " + str(right) + " is " + str(less_than))
print(str(left) + " >= " + str(right) + " is " + str(at_least))
print(str(left) + " == " + str(right) + " is " + str(equal))
print(str(left) + " != " + str(right) + " is " + str(not_equal))