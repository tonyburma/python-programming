# File name: test.py
def sum(x, y):
  return x + y

def multiply(x, y):
  return x * y  

def subscract(x, y):
  return x - y

def divide(x, y):
  if y == 0:
    raise ValueError("Cannot divide by zero.")
  return x / y

def debug_test():
  print(sum(5,3))
  print(f"__name__ in math_operations:: {__name__}")

if __name__ == "__main__":
  debug_test()