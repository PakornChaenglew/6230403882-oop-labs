def checks(x):
    B = False
    while not B:
        check = str(input(x))
        try:
            check = int(check)
        except ValueError:
            print("Please enter a number")
        else:
            return check


def checkopt(i):
    C = False
    while not C:
        y = str(input(i))
        try:
            if y == "+" or y == "-" or y == "*" or y == "/" or y == "//":
                if y == "+":
                    ans = num1 + num2
                elif y == "-":
                    ans = num1 - num2
                elif y == "*":
                    ans = num1 * num2
                elif y == "/":
                    if num2 == 0:
                        print("Cannot perform division by zero")
                        break
                    ans = num1 / num2
                print("Result of", num1, y, num2, "is", ans)
                C = True
            else:
                print("Unknown operator.")
                C = False
        except ValueError:
            print("Please enter an operator")

if __name__ == '__main__':
    A = False
    while not A:
        try:
            num1 = checks("Please enter the first operand:")
            num2 = checks("Please enter the second operand:")
            opt = checkopt("Please enter an operator (+,-,*,/):")
            break
        except ValueError:
            print("Error 404")