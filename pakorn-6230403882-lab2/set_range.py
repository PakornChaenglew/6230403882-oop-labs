a = {1, 2, 3, 4}
b = {1, 3, 5, 7}
c = a | b
d = a - b
print("a is", a)
print("b is", b)
print("a | b is", c)
print("a - b is", d)

ab = []
ac = []
ad = []
for n in range(20):
    ab.append(n)

x = range(3, 13)
for n in x:
    ac.append(n)

y = range(2, 51, 3)
for n in y:
    ad.append(n)

print(ab)
print(ac)
print(ad)
