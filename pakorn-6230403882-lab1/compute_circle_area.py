import math

i = 0

while True:
    i += 1

    Number1 = int(input("Enter radius :"))

    area = math.pi*(Number1)**2

    print("The  of radius ", Number1, " is %.2f" % area)

    if i == 2:
        break
