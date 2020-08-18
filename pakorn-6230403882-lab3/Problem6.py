months = ("January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October",
          "November", "December")
days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

month_dict = {}

for i in range(len(months)):
    month_dict.update({months[i]: days[i]})
    month_dict.items()
i = str(input("Enter month:"))
print("Number of days in", i, "is",month_dict[i])
