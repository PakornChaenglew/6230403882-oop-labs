a = [
    (1,),
    (2, 2),
    (3, 3, 3),
]

b = [
    list(range(10)),
    list(range(10, 20)),
    list(range(20, 30)),
    list(range(30, 40)),
]
print(a[1][1])
print(b[0][-2:])
