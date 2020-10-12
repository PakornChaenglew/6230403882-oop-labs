class Pet:

    def __init__(self, name):
        self.name = name

    def move(self):
        return  print(f"moving...")

    def show_info(self):
        return print(f"I'm {self.name}")

class Cat(Pet):
    def __init__(self, name, ownname, color):
        self.ownname = ownname
        self.color = color
        super().__init__(name)

    def __str__(self):
        return self.name

    def move(self):
        return  print(f"Cat likes to walk more than run")

    def show_info(self):
        return print(f"I'm {self.name} \n"
                     f"and is {self.color} \n"
                     f"belonging to {self.ownname}")

class Dog(Pet):
    def __init__(self, name, ownname, color):
        self.ownname = ownname
        self.color = color
        super().__init__(name)

    def move(self):
        return  print(f"Dog likes to run more than walk")

    def show_info(self):
        return print(f"I'm {self.name} \n"
                     f"and is {self.color} \n"
                     f"belonging to {self.ownname}")

    def eat_cat(self, cat):
        return print(f"Dog {self.name} eats cat {cat.name}")

if __name__ == '__main__':
    pet1 = Pet("Thongdaeng")
    pet1.show_info()
    pet1.move()
    cat1 = Cat("Thongdee", "Manee", "white");
    cat1.show_info();
    cat1.move();
    dog1 = Dog("Thongdee", "Manee", "white");
    dog1.show_info();
    dog1.move();
    dog1.eat_cat(cat1)