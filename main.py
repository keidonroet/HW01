import pytest
import math


def classify_triangle(a, b, c):
    string = ""
    if a == b and b == c and a == b:
        string = "Equilateral Triangle"
    elif a == b or a == c or b == c:
        string = "Isosceles Triangle"
    else:
        string = "Scalene Triangle"
    if (a*a+b*b == c*c) or (c*c+b*b == a*a) or (a*a+c*c == b*b):
        string += " and a Right Triangle"
    else:
        string += " and not a Right Triangle"

    return string

print(classify_triangle(1, 1, math.sqrt(2)))


def test_equilandright():
    assert classify_triangle(5, 5, 5) == "Equilateral Triangle and a Right Triangle"


def test_equilandnot():
    assert classify_triangle(5, 5, 5) == "Equilateral Triangle and not a Right Triangle"


def test_isosandright():
    assert classify_triangle(1, 1, math.sqrt(2)) == "Isosceles Triangle and a Right Triangle"


def test_isosandnot():
    assert classify_triangle(5, 5, 10) == "Isosceles Triangle and not a Right Triangle"


def test_scalandright():
    assert classify_triangle(3, 4, 5) == "Scalene Triangle and a Right Triangle"


def test_scalandnot():
    assert classify_triangle(3, 5, 7) == "Scalene Triangle and not a Right Triangle"


def test_badtriangle():
    assert classify_triangle(-10, 10, -10) == "Bad Triangle"





