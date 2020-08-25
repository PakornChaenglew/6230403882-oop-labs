num = input("Enterr the list of number (delimited by a comma):")
numlist = num.split()
print(numlist)
index = int(input("Enter an index:"))

try:
    print(numlist[index])
except IndexError:
    print("The list has no element at index", index)