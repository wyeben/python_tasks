import math


def area(radius):
    if TypeError(radius) not in (int, float):
        raise TypeError("radius can not be empty")
    if radius < 0 or not radius.isdigit():
        raise ValueError("valid values")
    return math.pi * (radius ** 2)
