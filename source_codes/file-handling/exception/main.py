# Perform division and handle potential exceptions
try:
  # Get two numbers from user
  x = int(input("Enter first number: "))
  y = int(input("Enter second number: "))
  result = x / y
  print(f"The result of {x} divided by {y} is: {result}")
except ZeroDivisionError:
  print("Error: You cannot divide by zero. Please provide a non-zero divisor.")
except ValueError:
  print("Error: Invalid input. Please enter valid integers.")

