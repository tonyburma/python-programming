def display_menu():
  print("Choose your option:")
  print("1. Check Scholarship Eligibility")
  print("2. Exit")
  choice = input("Enter your choice: ")
  return choice

def check_scholarship_eligibility(name, age, score, attendance):
  if age >= 18 and age <=25:
    if score >= 80:
      if attendance >= 90:
        print(f"{name} is eligible for FULL Scholarship")
      else:
        print(f"{name} is eligible for PARTIAL Scholarship")
    elif score >=70 and score <= 84:
      if attendance >= 90:
        print(f"{name} is eligible for PARTIAL Scholarship")
      else:
        print(f"{name} is NOT eligible for Scholarship")
    else:
      print(f"{name} is NOT eligible for Scholarship")
  else:
    print(f"{name} is NOT eligible for Scholarship due to age")

def main():
  while True:
    choice = display_menu()
    if choice == '1':
      # Get user input for scholarship eligibility criteria
      name = input("Enter your name: ")
      age = int(input("Enter your age: "))
      score = float(input("Enter your score: "))
      attendance = float(input("Enter your attendance percentage: "))
      check_scholarship_eligibility(name, age, score, attendance)
    elif choice == '2':
      print("Exiting the program. Goodbye!")
      break
    else:
      print("Invalid choice. Please try again.")

# Double Underscore DUNDER variables
if __name__ == "__main__":
  main()