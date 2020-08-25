import sys

def divide(dividend, divisor):
    return dividend / divisor

def checks(x):
    while True:
        check = str(input(x))
        try:
            check = int(check)
            if check < 0:
                exit(0)
            else:
                return  check
        except ValueError:
            print("Please enter a number")
        else:
            return check


while True:
    try:
        dividend = checks("Please enter the dividend:")
        divisor = checks("Please enter the divisor:")
        if divisor == 0:
            print("Connot perform division by zero")
        else:
            answer = divide(dividend, divisor)
            print('The answer is: {}'.format(answer))
    except ValueError:
        print("Error")


