import os
import csv
# Initialize an empty list to store the data
file_path = os.path.join('data', 'employee.csv')
with open(file_path, mode='r') as f:
  data = f.readlines()[1:21]  # Read lines 2 to 21 of the file
  reader = csv.reader(f)
  rows = list(reader)
  column_names = rows[0]  # Assuming the first row contains column names
  for row in rows[1:]:  # Skip the header row and print only the second row
    print(f"{column_names[1]}: {row[1]}, {column_names[2]}: {row[2]}")  # Print the second and third columns of each row in the CSV file

   