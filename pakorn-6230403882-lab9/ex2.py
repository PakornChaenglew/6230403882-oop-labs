from abc import ABC, abstractmethod

class Image(ABC):

    @abstractmethod
    def __init__(self, name):
        self.name = name

    def load_image(self):
       return f"loading "

    def save_image(self):
       return f"saving "

class Bitmap(Image):

    def __init__(self):
        super(Bitmap, self).__init__("bitmap")

    def __str__(self):
        return f"bitmap file"

    def load_image(self, name):
        self.name = name
        return print(super().load_image() + str(self) + f" {self.name}")

    def save_image(self, name):
        self.name = name
        return print(super().save_image() + str(self) + f" {self.name}")


class Jpeg(Image):
    def __init__(self):
        super(Jpeg, self).__init__("f")

    def __str__(self):
        return f"jpeg file"

    def load_image(self, name):
        self.name = name
        return print(super().load_image() + str(self) + f" {self.name}")

    def save_image(self, name):
        self.name = name
        return print(super().save_image() + str(self) + f" {self.name}")

if __name__ == '__main__':
    bitmap1 = Bitmap()
    bitmap1.save_image("kku.bmp")
    bitmap1.load_image("kku.bmp")
    jpeg1 = Jpeg()
    jpeg1.save_image("en.jpg")
    jpeg1.load_image("en.jpg")
