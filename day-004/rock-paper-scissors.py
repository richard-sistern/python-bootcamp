import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

def print_move(move):
    if move == "Rock":
        print(rock)
    elif move == "Paper":
        print(paper)
    elif move == "Scissors":
        print(scissors)
    else:
        print("Unknown move...")

human_move = input("Enter your choice (Rock, Paper, Scissors): ")
print("You chose:")
print_move(human_move)

moves = ["Rock", "Paper", "Scissors"]
computer_move = random.choice(moves)
print("Computer chose:")
print_move(computer_move)

if human_move == computer_move:
    print("DRAW")
    print_move(human_move)
elif human_move == "Rock" and computer_move == "Scissors":
    print("YOU WON")
    print_move(human_move)
elif human_move == "Paper" and computer_move == "Rock":
    print("YOU WON")
    print_move(human_move)
else:
    print("YOU LOST")
    print_move(computer_move)