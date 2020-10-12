class Vehicle:
    def __init__(self, name, speed, mileage):
        self.name = name
        self.__speed = speed
        self.mileage = mileage

    def set_speed(self, speed):
        self.__speed = speed

    def get_speed(self):
        return self.__speed

class Car(Vehicle):

    def __init__(self, name, speed, mileage, num_doors):
        self.num_doors = num_doors
        super().__init__(name, speed, mileage)

    def __str__(self):
        return f"{self.name} speed: {self.get_speed()} mileage: {self.mileage} num doors:{self.num_doors}"

class Bus(Vehicle):

    def __init__(self, name, speed, mileage, num_doors):
        self.num_doors = num_doors
        super().__init__(name, speed, mileage)

    def __str__(self):
        return f"{self.name} speed: {self.get_speed()} mileage: {self.mileage} num doors:{self.num_doors}"


if __name__ == '__main__':
    car = Car("Toyota Vios", 90, 150000, 4)
    bus = Bus("Toyota Vios", 12, 200000, 100)
    print(car)
    print(bus)
    bus.set_speed(30)
    print(bus)