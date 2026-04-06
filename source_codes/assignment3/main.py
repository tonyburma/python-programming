import csv

file_path = "products-100000.csv"

def display_menu():
  print("\n--Product Catalog Menu--")
  print("1. View all products")
  print("2. Total Inventory Value")
  print("3. Low Stock Products")
  print("4. Category Search")
  print("5. Average Price by Brand")
  print("6. Exit")
  choice = input("Enter your choice: ")
  return choice

def view_all_products():
  with open(file_path, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
      print(f"ID: {row['Index']}, Name: {row['Name']}, Category: {row['Category']}, Price: ${row['Price']}, Stock: {row['Stock']}")

def total_inventory_value():
  total = 0
  with open(file_path, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
      total += float(row['Price']) * int(row['Stock'])
    
  print(f"Total Inventory Value: ${total:.2f}")

def low_stock_products():
  threshold = 10
  print(f"Products with stock less than {threshold}:")
  with open(file_path, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
      if int(row['Stock']) < threshold:
        print(f"ID: {row['Index']}, Name: {row['Name']}, Stock: {row['Stock']}")

def category_search():
  category = input("Enter category to search: ")
  print(f"Products in category '{category}':")
  with open(file_path, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
      if category.lower() in row['Category'].lower():
        print(f"Name: {row['Name']}, {row['Category']}")

def avg_price_by_brand():
  brand = input("Enter brand to calculate average price: ")
  total_price = 0
  count = 0
  with open(file_path, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
      if row['Brand'].lower() == brand.lower():
        total_price += float(row['Price'])
        count += 1
  if count > 0:
    avg_price = total_price / count
    print(f"Average price for brand '{brand}': ${avg_price:.2f}")
  else:
    print(f"No products found for brand '{brand}'")


def main():
  while True:
    choice = display_menu()
    match choice:
      case "1":
        view_all_products()
      case "2":
        total_inventory_value()
      case "3":
        low_stock_products()
      case "4":
        category_search()
      case "5":
        avg_price_by_brand()
      case "6":
        print("Exiting the program. Goodbye!")
        break
      case _:
        print("Invalid choice. Please try again.")


if __name__ == "__main__":
  main()
