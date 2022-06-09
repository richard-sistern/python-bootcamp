# on every year that is evenly divisible by 4
# except every year that is evenly divisible by 100
# unless the year is also evenly divisible by 400

year = int(input("Which year do you want to check? "))

# Rework previous version I did in Ruby
if (year % 4 == 0 and year % 100 !=0) or year % 400 == 0:
    print("Leap year")
else:
    print("Not a leap year")