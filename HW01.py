import pytest


def classify_triangle(a, b, c):

    if a <= 0 or b <= 0 or c <= 0:
        return str("That is not a Triangle!")
    elif a == b and b == c and a == b:
        return str("Equilateral Triangle")
    elif a**2 + b**2 == c**2:
        return str("Right Triangle")
    elif a == b or b == c or a == c:
        return str("Isosceles Triangle")
    else:
        return str("Scalene Triangle")


def test():
    assert classify_triangle(100, 50, 100) == "Isosceles Triangle"
    assert classify_triangle(3, 4, 5) == "Right Triangle"
    assert classify_triangle(1, 1, 1) == "Equilateral Triangle"
    assert classify_triangle(0, 0, 0) == "That is not a Triangle!"
    assert classify_triangle(-1, 1, 0) == "That is not a Triangle!"
    assert classify_triangle(1, 2, 3) == "Scalene Triangle"


