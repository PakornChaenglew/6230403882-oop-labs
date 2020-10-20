from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def __init__(self, name):
        self.name = name

class Human(Animal):

    def __init__(self):
        super(Human, self).__init__("Human")

    def move(self):
        return print(f"I can walk and run")


class Snake(Animal):
    def __init__(self):
        super(Snake, self).__init__("Snake")

    def move(self):
        return print(f"I can crawl")


class Dog(Animal):
    def __init__(self):
        super(Dog, self).__init__("Dog")

    def move(self):
        return print(f"I can bark")

if __name__ == '__main__':
    human = Human()
    human.move()
    snake = Snake()
    snake.move()
    dog = Dog()
    dog.move()