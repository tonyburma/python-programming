class Student:
  def __init__(self, student_id, name, course, marks):
    self.student_id = student_id
    self.name = name
    self.course = course
    self.marks = marks

  def display_info(self):
    print(f"ID: {self.student_id}, Name: {self.name}, Course: {self.course}, Marks: {self.marks}")

  def is_pass(self):
    if self.marks >=50:
      return "Pass"
    else:
      return "Fail"

student1 = Student(1, "Alice", "Mathematics", 85)
student2 = Student(2, "Bob", "Physics", 90)
student3 = Student(3, "Charlie", "Chemistry", 78)
student4 = Student(4, "David", "Biology", 92)
student5 = Student(5, "Eve", "Computer Science", 40)

students = [student1, student2, student3, student4, student5]

obj_list = [
  Student(6, "Frank", "Mathematics", 65), 
  Student(7, "Grace", "Physics", 55),
  Student(8, "Heidi", "Chemistry", 45),
  Student(9, "Ivan", "Biology", 80),
  Student(10, "Judy", "Computer Science", 70)
]

def main():
  for student in students:
    student.display_info()
    print(f"Result: {student.is_pass()}\n\n")

def add_student():
  student_id = int(input("Enter student ID: "))
  name = input("Enter student name: ")
  course = input("Enter student course: ")
  marks = int(input("Enter student marks: "))
  
  new_student = Student(student_id, name, course, marks)
  students.append(new_student)
  print("Student added successfully.")


if __name__ == "__main__":
  main()