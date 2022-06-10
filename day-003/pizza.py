print("PIZZA PIZZA PIZZA")

size = input("What size do you want? S, M, L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0


if size == "S":
    bill += 15 # Small
elif size == "M":
    bill += 20 # Medium
elif size == "L":
    bill += 25 # Large
else:
    print("Borked order...")

if add_pepperoni == "Y":
    if size == "S":
        bill += 2 # Small
    elif size == "M" or size == "L":
        bill += 3 # Medium/Large
    else:
        print("Borked pepperoni...")

if extra_cheese == "Y":
    bill += 1 # Cheese

print(f"Your total bill is ${bill}")