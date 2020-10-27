class Shape:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return f"Drawing a"

class Circle(Shape):
    n = 0
    globals()['n'] = n

    def __init__(self, color, radius):
        self.radius = radius
        super().__init__(color)

    def set_radius(radius):
        self.__radius = radius

    def radius(self, radius):
        return int(radius)

    def draw(self):
        global n
        while True:
            n += 1
            return print(super().__str__() + f"circle with radius {self.radius}")

    def get_num_circles():
        return n

class Rectangle(Shape):
    e = 0
    globals()['e'] = e

    def __init__(self, color, width, height):
        self.width = width
        self.height = height
        super().__init__(color)

    def set_width(self, width):
        self.__width = width

    def width(self, width):
        return int(width)

    def set_height(self, height):
        self.__height = height

    def height(self, height):
        return int(height)

    def draw(self):
        return print(super().__str__() + f"rectangle with width {self.width} height {self.height}")

    def print_area(self):
        global e
        while True:
            e += 1
            area = self.width * self.height
            return print(f"Rectangle width {self.width} height {self.height} has area as {area}")

    def get_num_rectangles():
        return e
