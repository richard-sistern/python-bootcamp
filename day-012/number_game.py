#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random

def set_difficulty(difficulty):
    if difficulty == 'easy':
        return 10
    elif difficulty == 'hard':
        return 5
    else:
        return 0

        
def make_a_guess(guesses):
    print(f"You have {guesses} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess == random_number:
        print("Correct!")
        return True
    
    if guess > random_number:
        print("Too high.")
    else:
        print("Too low.")

    print("Guess again.")
    return False

from logo import logo
print(logo)

random_number = random.randint(1, 100)
print(random_number)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number betwen 1 and 100")
# play_game()

difficulty = input("Choose a difficulty.  Type 'easy' or 'hard': ")
guesses = int(set_difficulty(difficulty))

for i in range(guesses, 0, -1):
    result = make_a_guess(i)
    if result:
        break
    #guesses -= 1