import random

from art import logo, vs
from game_data import data

print(logo)



# DONE: Grab a random choice from data
def new_option():
    return random.choice(data)


current_score = 0
correct_answer = True

option_a = new_option()
option_b = new_option()

while correct_answer:

    if current_score > 0:
        print(f"You're right! Current score: {current_score}.")
        
    print(f'Compare A: {option_a["name"]}, a {option_a["description"]}, from {option_a["country"]}.')

    print(vs)

    print(f'Compare B: {option_b["name"]}, a {option_b["description"]}, from {option_b["country"]}.')

    answer = input("Who has more followers? Type 'A' or 'B': ")

    if answer == "A" and option_a["follower_count"] > option_b["follower_count"]:
        current_score += 1

        option_a = option_b
        option_b = new_option()
    elif answer == "B" and option_b["follower_count"] > option_a["follower_count"]:
        current_score += 1

        option_a = option_b
        option_b = new_option()
    else:
        correct_answer = False

print(f"Sorry, that's wrong. Final score: {current_score}")