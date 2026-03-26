def main():
  name: str = input("Enter the student name: ")
  age: int = int(input("Enter the student age: "))
  score: float = float(input("Enter the student score: "))
  attendance: float = float(input("Enter the student attendance percentage: "))
  

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


if __name__ == "__main__":
  main()