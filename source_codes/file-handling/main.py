# import lib

def display_menu():   
     while True:
        print("1. Read the file")
        print("2. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            choice_1_function()
        if choice == "2":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

def choice_1_function():
    print("You chose to read the file.")
    # Call the function to read the file here
    # For example, you can call a function from csv_reader.py or files.py

def main():
   display_menu()

if __name__ == "__main__":
    main()