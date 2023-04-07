################### Scope ####################

enemies = 1 # Global scope

def increase_enemies():
  enemies = 2 # Local scope
  print(f"enemies inside function: {enemies}")


def increase_enemies_global():
  global enemies # Should be avoided where possible
  enemies +=2 # Local scope
  print(f"enemies inside function with global: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

increase_enemies_global()


# The right  way to modify global scope from a func
def increase_enemies_proper():
  return enemies + 1 

enemies = increase_enemies_proper()
print(enemies)

# Global constants
PI = 3.14 # Naming convention is to uppercase constants