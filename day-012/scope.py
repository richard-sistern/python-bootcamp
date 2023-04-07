################### Scope ####################

enemies = 1 # Global scope

def increase_enemies():
  enemies = 2 # Local scope
  print(f"enemies inside function: {enemies}")


def increase_enemies_global():
  global enemies
  enemies +=2 # Local scope
  print(f"enemies inside function with global: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

increase_enemies_global()