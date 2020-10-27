def sum(x, y):
    return x + y

def subtract(x, y):
    return x - y

def mul(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError
    else:
        return x / y
