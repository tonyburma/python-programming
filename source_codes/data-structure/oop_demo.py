class Student:
  def __init__(self, first_name, last_name, grade):
    self.first_name = first_name
    self.last_name = last_name
    self.grade = grade

  def display_info(self):
    print(f"Student Name: {self.first_name} {self.last_name}, Grade: {self.grade}")

def main():
  # Creating student instances (objects)
  # Objects are instances of a class, which is a blueprint for creating objects.
  student1 = Student("Alice", "Johnson", "A")
  student2 = Student("Bob", "Smith", "B")

  student1.display_info()
  student2.display_info()

  print("Student 1's first name:", student1.first_name) # Object.attribute access
  print("Student 2's last name:", student2.last_name)

  # List of students
  students = [student1, student2]

  # Display information for all students
  for x in students:
    x.display_info()


if __name__ == "__main__":
  main()
