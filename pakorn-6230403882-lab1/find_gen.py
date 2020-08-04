import datetime

Name = str(input("Enter your name: "))
Born = input("Enter the year were born: ")

Born = int(Born)
Year = datetime.datetime.now()
Year = int(Year.year)

Age = Year - Born

if 1 <= Age <= 9:
    Gen = "Alpha"
elif 10 <= Age <= 24:
    Gen = "Z"
elif 25 <= Age <= 39:
    Gen = "Y"
elif 40 <= Age <= 54:
    Gen = "X"
elif 55 <= Age <= 72:
    Gen = "Baby Boomer"
elif 73 <= Age:
    Gen = "Buider"

print(Name, " is ", Age, " year old. You are generation ", Gen)
