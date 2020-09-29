class Numbers:

    def __init__(self, x, y):
        self.number1 = x
        self.number2 = y

    def add(self):
        sum = self.number1 + self.number2
        return sum

    def display(self):

    @classmethod
    def display_factor(cls, number1):
        if number1 % 2 == 0:
            cls.ans1 = number1 / 2
            cls.ans2 = number1 / 2
        elif number1 % 2 != 0:
            cls.ans1 = (number1 / 2) + 0.5
            cls.ans2 = (number1 / 2) - 0.5
        return f"Factor of {number1} is {cls.ans1} and {cls.ans2}"

    @staticmethod
    def is_valid_divisor(number2):
        if number2 > 0:
            return f"{number2} is a valid divisor"
        elif number2 <= 0:
            return f"{number2} is not a valid divisor"

if __name__ == '__main__':
    print(f"3 + 5 is {Numbers(3,5).add()}")
    print(Numbers.display_factor(6))
    print(Numbers.display_factor(8))
    print(Numbers.is_valid_divisor(2))
    print(Numbers.is_valid_divisor(0))
