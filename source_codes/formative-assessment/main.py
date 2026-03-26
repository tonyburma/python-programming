import os

# Get the current working directory
current_directory = os.getcwd()
print(f"Current working directory: {current_directory}")

# List all files and directories in the current working directory
files_and_directories = os.listdir(current_directory)
print("Files and directories in the current working directory:")
for item in files_and_directories:
    print(item)

# Chage to /user/source directory
# new_directory = "/Users/tonytoe/source"
# os.chdir(new_directory)
# print(f"Changed to new directory: {os.getcwd()}")

# os.makedirs("reports/2026")

# Rename a file
# os.chdir("reports/2026")
# os.rename("data.txt", "data_backup.txt")

# os.remove("data_backup.txt")

path = os.path.join("data", "raw", "data.txt")
print(f"Path to data.txt: {path}")