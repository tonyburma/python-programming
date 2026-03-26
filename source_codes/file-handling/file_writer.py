import os

file_path = os.path.join('data', "new_file.txt")

try:
  if not os.path.exists(file_path):
    with open(file_path, mode='w') as file:
      file.write("This is a new file created using Python.\n")
      file.write("You can write multiple lines to the file.\n")
      file.write("Make sure to close the file after writing.")
  else:
    print(f"The file '{file_path}' already exists. No new file was created.")
    with open(file_path, mode='a') as f:
      f.write("Extra line of text.\n")
      f.write("Another extra line of text.\n")
except Exception as e:
  print(f"An error occurred: {e}")




