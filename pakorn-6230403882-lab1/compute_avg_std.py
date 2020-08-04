import math
import random

i = 0

while True:
    i += 1

    Number1 = random.randint(1, 10)
    Number2 = random.randint(1, 10)

    avg = (Number1+Number2)/2
    std = math.sqrt((((Number1-avg)**2)+((Number2-avg)**2))/2)

    print("The averag of", Number1, "and", Number2, "is ", avg)
    print("The standard deviation of", Number1, "and", Number2, "is ", std)

    if i == 3:
        break
