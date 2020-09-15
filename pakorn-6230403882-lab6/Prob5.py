import json
data =  {
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"]
}
with open("hobbies.json", 'w') as o:
    json.dump(data, o)
