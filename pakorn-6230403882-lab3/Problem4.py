num = int(input("Enter a number to find the factorial:"))
number = num
total = 1
while num > 0:
    total = total * (num)
    num -= 1
print("Factorial of", number, "is", total)
