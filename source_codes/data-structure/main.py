import bisect
import math_operations

def main():
  numbers = [5, 4, 3, 2, 1, 3] # List'''
  new_numbers = sorted(numbers)
  print(new_numbers)
  print("Original list:", numbers )

  print(sorted(numbers))

  print(3 in numbers)

  # Binary search using bisect
  pos = bisect.bisect_right(new_numbers, 3)
  print("Found at index:", pos)

  # Sets
  my_set = set(numbers) # Set
  print("Unique numbers:", my_set)

  # Dictionaries
  person1 = {"first_name": "John", "last_name": "Smith"} # Dictionary
  print("Dictionary:", person1)

  # Tuples
  person_tuple = ("John", "Smith") # Tuple
  print("Tuple:", person_tuple[0], person_tuple[1])

if __name__ == "__main__":
  main()