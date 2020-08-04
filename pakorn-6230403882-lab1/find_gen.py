import datetime
Name = str(input("Enter your name: "))
Born = input("Enter the year were born: ")
Born = int(Born)
Year = datetime.datetime.now()
Year = int(Year.year)
Age = Year - Born
if 1 <= Age <= 9:
    Gen = "Alpha"
    print(Name, " is ", Age, " year old. You are generation ", Gen)
elif 10 <= Age <= 24:
    Gen = "Z"
    print(Name, " is ", Age, " year old. You are generation ", Gen)
elif 25 <= Age <= 39:
    Gen = "Y"
    print(Name, " is ", Age, " year old. You are generation ", Gen)
elif 40 <= Age <= 54:
    Gen = "X"
    print(Name, " is ", Age, " year old. You are generation ", Gen)
elif 55 <= Age <= 72:
    Gen = "Baby Boomer"
    print(Name, " is ", Age, " year old. You are generation ", Gen)
elif 73 <= Age:
    Gen = "Buider"
    print(Name, " is ", Age, " year old. You are generation ", Gen)
else:
    print("ERROR")
