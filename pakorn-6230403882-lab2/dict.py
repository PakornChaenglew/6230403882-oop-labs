directory = {
    "Jane Doe": "+27 555 1024",
    "John Smith": "+27 555 6254",
    "Bob Stone": "+27 555 5689",
    "Anna Cooper": "+27 555 3237"
}

print(directory["Bob Stone"])
print(directory.get("Bob Stone", None))

print(directory.keys())
print(directory.values())
