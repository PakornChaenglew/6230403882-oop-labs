import math

class Circle:
    def __init__(self, r):
        self.radius = r

    def print(self):
        return self.radius

    def area(self):
        ans = math.pi * math.pow(self.radius, 2)
        return ans

    def perimeter(self):
        perimeter = 2 * math.pi * self.radius
        return perimeter

if __name__ == '__main__':
    print("The circle with radius {} has the area as {:.2f} \n"
          "ans the perimeter as {:.2f}".format(Circle(3).print(), Circle(3).area(), Circle(3).perimeter()))
    print("The circle with radius {} has the area as {:.2f} \n"
          "ans the perimeter as {:.2f}".format(Circle(4).print(), Circle(4).area(), Circle(4).perimeter()))
