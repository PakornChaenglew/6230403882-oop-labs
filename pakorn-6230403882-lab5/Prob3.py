import math

def hypotenuse(c, d):
    try:
        return math.sqrt(math.pow(c,2)+math.pow(d,2))
    except TypeError:
        return None

print("hypotenuse({}, {}) is {}".format(3.0, 4.0, hypotenuse(3, 4)))
print("hypotenuse({}, {}) is {}".format("3", "4", hypotenuse("3", "4")))
print("hypotenuse({}, {}) is {}".format(3.0, "4.0", hypotenuse(3.0, "4.0")))
