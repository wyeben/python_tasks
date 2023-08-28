class Point:
    default_color = "blue"

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value): 
        if value < 0:
            raise ValueError("x value cannot be negative")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if value < 0:
            raise ValueError("y value cannot be negative")
        self.__y = value

    def draw(self):
        print(f"drawing at point ({self.__x}, {self.__y})")

    def __str__(self):
        return f"({self.__x}, {self.__y})"

    def __eq__(self, other):
        return self.__x == other.x and self.__y == other.y

    def __add__(self, other):
        return Point(self.__x + other.x, self.__y + other.y)


Point.default_color = "red"
p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = p1 + p2
print(p3)

print(p1 + p2)
print(p2.default_color)