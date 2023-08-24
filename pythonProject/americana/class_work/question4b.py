import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2


def main():
    try:
        radius = float(input("Enter the radius of the circle: "))
        circle = Circle(radius)
        area = circle.calculate_area()
        print(f"The area of the circle with radius {radius} is {area:.2f}")
    except ValueError:
        print("Please enter a valid numeric value for the radius.")


if __name__ == "__main__":
    main()
