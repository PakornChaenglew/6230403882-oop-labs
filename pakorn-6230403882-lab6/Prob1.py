name = (2, 10, 11, 3)
set = []
for n in name:
    file = "filel_:{:04}".format(n)
    set.append(file)
print("{:30}{}".format("input filename are",name))
print("{:30}{}".format("zero paddaed filenames",set))
set.sort()
print("{:30}{}".format("sorted filenames are",set))
