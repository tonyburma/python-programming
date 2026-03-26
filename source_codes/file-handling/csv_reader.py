import os
import csv

# Initialize an empty list to store the data
employee_list = []

file_path = os.path.join('data', 'employee.csv')

# Open the CSV file and read its contents
with open(file_path, mode='r') as file:
  csv_reader = csv.reader(file)
  
  for row in csv_reader:
    employee_list.append(row)

# Print the list of employees
for e in employee_list:
  print(e)  # Assuming the CSV has three columns: Name, Age, Department
  print('-'*50)

