weight = input("What is your weight in KG? ")
height = input("What is your height in m? ")

bmi = float(weight) / float(height) ** 2

print("Your bmi is " + str(int(bmi)))