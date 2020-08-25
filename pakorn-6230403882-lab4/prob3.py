import sys

def divide(dividend, divisor):
    return dividend / divisor

def checks(x):
    while True:
        check = str(input(x))
        try:
            check = int(check)
        except ValueError:
            print("Please enter a number")
        else:
            return check

while True:
    try:
        dividend = checks("Please enter the dividend:")
        divisor = checks("Please enter the divisor:")
        if dividend < 0 or divisor < 0:
	        break
        elif divisor == 0:
            break
        answer = divide(dividend, divisor)
        print('The answer is: {}'.format(answer))
    except ValueError:
        print("Error")


