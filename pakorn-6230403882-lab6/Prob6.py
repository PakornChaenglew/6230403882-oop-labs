import json
with open("hobbies.json", 'r') as o:
    a = json.load(o)
    f = a["hobbies"]
    p = ", ".join(f)
    print(a["firstName"],"has hobbies as",p)
