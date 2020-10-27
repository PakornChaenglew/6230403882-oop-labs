import random
import shape

if __name__ == '__main__':
    circles = []
    rectangles = []
    NUM_OBJECTS = 10
    MIN = 10
    MAX = 20
    colors = ["green", "yellow", "blue", "red", "pink"]
    for i in range(NUM_OBJECTS):
        colors = random.choice(colors)
        radius = random.randint(MIN, MAX)
        circles.append(shape.Circle(colors, radius))
        circles[i].draw()
    print(f"Num circles is {shape.Circle.get_num_circles()}")

    for i in range(NUM_OBJECTS):
        colors = random.choice(colors)
        width = random.randint(MIN, MAX)
        height = random.randint(MIN, MAX)
        rectangles.append(shape.Rectangle(colors, width, height))
        rectangles[i].draw()
        rectangles[i].print_area()
    print(f"Num rectangles is {shape.Rectangle.get_num_rectangles()}")