class Shape:
    def __init__(self, color):
        self.color = color

class Circle(Shape):

    def __init__(self, color, radius):
        self.radius = radius
        super().__init__(color)

    def set_radius(radius):
        self.__radius = radius

    def radius(self, radius):
        return int(radius)

class Rectangle(Shape):

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
