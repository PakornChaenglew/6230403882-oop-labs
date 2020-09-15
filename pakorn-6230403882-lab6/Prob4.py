with open("kku2.txt", 'w', encoding='utf8') as f:
    with open("kku.txt", encoding="utf-8") as o:
        pr = o.read()
        g = "\nMotto: วิทยา จริยา ปัญญา\nMotto in English: Knowledge"
    f.write(pr)
    f.write(g)
with open("kku2.txt", encoding='utf8') as e:
    p = e.read()
    print(p)