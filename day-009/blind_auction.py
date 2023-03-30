from blind_auction_art import logo

print(logo)
print("Welcome to the secret auction program.")

auction = {}

response = 'yes'
while response == 'yes':
    name = input("What is your name?: ")
    bid = input("What's your bid?: ")

    auction[name] = bid

    response = input("Are there any other bidders? Type 'yes' or 'no'.\n")

winner = max(auction)
print(f"The winner is {winner} with a bid of {auction[winner]}")