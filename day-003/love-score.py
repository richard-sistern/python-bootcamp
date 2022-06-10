name1 = input("What is your name? ")
name2 = input("What is their name? ")

names = name1.lower() + name2.lower()

true_total = 0

true_total += names.count("t")
true_total += names.count("r")
true_total += names.count("u")
true_total += names.count("e")

love_total = 0

love_total += names.count("l")
love_total += names.count("o")
love_total += names.count("v")
love_total += names.count("e")

love_score = int(str(true_total) + str(love_total))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")