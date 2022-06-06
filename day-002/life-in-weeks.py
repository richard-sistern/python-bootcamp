AGE_TARGET = 90

age = input("What is your current age?\n")
age_as_int = int(age)

years_remaining = AGE_TARGET - age_as_int
months_remaining = years_remaining * 12
weeks_remaining = years_remaining * 52
days_remaining = years_remaining * 365

print(f"Remaining - Years: {years_remaining}, Months: {months_remaining}, Weeks: {weeks_remaining}, Days: {days_remaining}")