def fac(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return n * fac(n-1)

if __name__ == '__main__':

    try:
        n = input("Enter an integer:")
        n = int(n)
        if n < 0:
            print("Please enter a positive integer. {} is not a positive integer".format(n))
        else:
            print("factorial {} is {}".format(n, fac(n)))
    except ValueError:
        n = str(n)
        print("Please enter a positive integer. invalid literal for int() with base 10: {} ".format(n))
