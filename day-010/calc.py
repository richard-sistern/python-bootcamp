# Calculator

operations = {
  "+": "add",
  "-": "subtract",
  "*": "multiply",
  "/": "divide"
}

# Add
def add(n1, n2):
  return n1 + n2

# Subtract
def subtract(n1, n2):
  return n1 - n2

# Multiply
def multiply(n1, n2):
  return n1 * n2

# Divide
def divide(n1, n2):
  return n1 / n2

from calc_art import logo
print(logo)

num1 = int(input("What's the first number?: "))

for symbol in operations:
  print(symbol)

operation_symbol = input("Pick an operation from the line above: ")

num2 = int(input("What's the second number?: "))

if operation_symbol not in operations:
  print("Invalid operation symbol")
else:
  calc_function = operations[operation_symbol]
  answer = calc_function(num1, num2)

  print(f"{num1} {operation_symbol} {num2} = {answer}") #