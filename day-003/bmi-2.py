height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = round(weight / height ** 2)

if bmi < 18.5:
    advice = "underweight"
elif bmi < 25:
    advice = "normal weight"
elif bmi < 30:
    advice = "overweight"
elif bmi < 35:
    advice = "obese"
else:
    advice = "clinically obese"



print(f"Your BMI is {bmi}, you are {advice}")