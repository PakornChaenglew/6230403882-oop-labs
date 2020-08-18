months = ("January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October",
          "November", "December")
days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

month_dict = dict(zip(months, days))
i = str(input("Enter month:"))
print("Number of days in", i, "is",month_dict[i])