def greet(name):
    print(f"PEW {name}")
    print(f"PEW {name}")
    print(f"PEW {name}")

greet("Biff")

def greet_with(name, location):
    print(f"Pew {name}")
    print(f"in the {location}")

# Positional
greet_with("Marty", "future")

# Keyword
greet_with(name = "Doc", location = "past")