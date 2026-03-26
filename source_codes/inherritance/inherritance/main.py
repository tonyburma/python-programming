class Person:
  def __init__(self, id, name, email, phone, type, dob):
    self.id = id
    self.name = name
    self.email = email
    self.phone = phone
    self.type = type
    self.dob = dob
  
  def display_info(self):
    print()
    print(f"Type: {self.type}")
    print(f"ID: {self.id}")
    print(f"Name: {self.name}")
    print(f"Email: {self.email}")
    print(f"Phone: {self.phone}")
    # print()

class Student(Person):
  def __init__(self, id, name, email, phone, enrollment_number, dob):
    super().__init__(id, name, email, phone, "Student", dob)
    self.student_id = id
    self.enrollment_number = enrollment_number
    # self.dob = dob

  def display_info(self):
    super().display_info()
    print(f"Enrollment Number: {self.enrollment_number}")
    print(f"Date of Birth: {self.dob}")

class Lecturer(Person):
  def __init__(self, id, name, email, phone, dob):
    super().__init__(id, name, email, phone, "Lecturer", dob)
    self.lecturer_id = id

class Staff(Person):
  def __init__(self, id, name, email, phone, dob):
    super().__init__(id, name, email, phone, "Staff", dob)
    self.staff_id = id

def main():
  student1 = Student(1, "Alice", "alice@example.com", "123-456-7890", "EN-0019191", "2000-01-01")
  lecturer1 = Lecturer(2, "Bob", "bob@example.com", "098-765-4321", "1980-05-15")
  staff1 = Staff(3, "Charlie", "charlie@example.com", "555-555-5555", "1990-10-10")

  student1.display_info()
  lecturer1.display_info()
  staff1.display_info()

if __name__ == "__main__":
  main()