A = False

while not A:
    try:
        tf = int(input("Enter a temperature in Fahrenheit:"))
        tc = (5 / 9) * (tf - 32)
        print("Temperature", tf, "in Fahrenheit is %.2f" % tc, "in celsius")
    except ValueError:
        print("Please enter a valid floating point for the temperature.")
    else:
        A = True
