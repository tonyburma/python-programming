'''Decorator function'''
from time import time


def log(func):
  def wrapper():
    print("Function started!")
    
    func()
    print("Function ended!")
  return wrapper

@log
def say_hello():
  # print("Function started!")
  print("Hello!")
  # print("Function ended!")

@log
def say_goodbye():
  # print("Function started!")
  print("Goodbye!")
  # print("Function ended!")



say_hello()
say_goodbye()