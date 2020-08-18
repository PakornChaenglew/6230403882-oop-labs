i = 0
sum = 0
loop = [1]
A = False

while not A:
    try:
        for i in loop:
            number = int(input("Enter an integer:"))
            if number > 0:
                sum += number
                loop.append(i+1)
                A = True
            if number < 0 and i != 0:
                average = sum / (i - 1)
                print(average)
                A = True
                break
            if number < 0 and i == 0:
                print("You haven't entered a positive number")
                A = True
                break
    except ValueError:
        print("Error")

