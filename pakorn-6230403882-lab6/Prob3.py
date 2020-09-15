read = input(">>>")

with open(read, encoding='utf8') as f:
    for line in f:
        print(line, end='')
