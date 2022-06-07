print("Welcome to the tip calculator...")
bill = float(input("What was the total bill? "))
tip = int(input("What percentage would you like to tip? "))
people = int(input("Number of people to split the bill? "))

bill_with_tip = tip / 100 * bill + bill

print(bill_with_tip)

bill_per_person = "{:.2f}".format(bill_with_tip / people)

print(f"Each person should pay {bill_per_person}")