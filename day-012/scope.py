################### Scope ####################

enemies = 1 # Global scope

def increase_enemies():
  enemies = 2 # Local scope
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")