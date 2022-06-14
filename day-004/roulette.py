names_input = input("List of names, seperated by a comma. ")

names = names_input.split(", ")

import random

#random_int = random.randint(0, len(names) - 1)

print(random.choice(names))