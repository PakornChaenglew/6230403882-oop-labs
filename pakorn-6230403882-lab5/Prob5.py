import math

def checks(x):
    B = False
    while not B:
        check = str(input(x))
        if check.lower() == "q":
            return check
        else:
            try:
                check = float(check)
                return check
            except ValueError:
                print("Please enter a number")
            else:
                return check

def cal(a, b, i):
    C = False
    while not C:
        try:
            a = float(a)
            b = float(b)
            i = str(i)
            if i == "+" or i == "-" or i == "*" or i == "/" or i == "//":
                if i == "+":
                    z = a + b
                elif i == "-":
                    z = a - b
                elif i == "*":
                    z = a * b
                elif i == "/":
                    if b == 0:
                        print("Cannot perform division by zero")
                        break
                    z = a / b
                C = True
                return z
            else:
                z = a + b
                C = True
                return z
        except ValueError:
            print("Please enter an operator")

if __name__ == '__main__':
    while True:
        o1 = checks("Please enter the first operand ('q' to quit):")
        if o1.lower() == "q":
            break
        o2 = checks("Please enter the second operand:")
        if o2 == "q" or o2 == "Q":
            break
        op = input("Please enter an operator (+,-,*,/):")
        if op == "q" or op == "Q":
            break
        op = str(op)
        fi = input("Enter output format (float, int):")
        if fi == "q" or fi == "Q":
            break
        if fi is None:
            continue
        out = cal(o1, o2, op)
        if fi == "int":
            out = int(round(out))
        if fi == "float":
            out = float(out)
        if out is not None:
            if op == "":
                op = "+"
            round(out)
            print("{} {} {} = {}".format(o1, op, o2, out))
        else:
            print("We cannot perform your requested calculation")