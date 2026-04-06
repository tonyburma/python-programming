import csv

file_path = 'products-100000.csv'

def display_menu():
    print("\n--- Product Catalog Menu ---")
    print("1. View products by category")
    print("2. Print All Product Names")
    print("3. Total Inventory Value")
    print("4. Low Stock Alert")
    print("5. Exit")

    user_choice = input("Enter your choice (1-5): ")
    return user_choice

def main():
    while True:
      user_choice = display_menu()
      match user_choice:
          case '1':
              view_products_by_category()
          case '2':
              print_all_product_names()
          case '3':
              total_inventory_value()
          case '4':
              low_stock_alert()
          case '5':
              print("Exiting the program. Goodbye!")
              break
          case _:
              print("Invalid choice. Please enter a number between 1 and 5.")
        
        
def view_products_by_category():
    # Prompt user for category
    category_input = input("Enter a Category (e.g., Electronics): ")

    # Open and read the CSV file
    with open(file_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        # Store matching products
        matching_products = []
        
        for row in reader:
            category = row['Category']
            
            # Check if the category matches (case-insensitive comparison)
            if category.lower() == category_input.lower():
                matching_products.append(row)
        
        # Display results
        if matching_products:
            print(f"\n--- Products in '{category_input}' category ---")
            for product in matching_products:
                print(f"Name: {product['Name']}, Price: ${product['Price']}, Stock: {product['Stock']}")
        else:
            print("No products found in this category.")

def print_all_product_names():
    with open(file_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        print("\n--- All Product Names ---")
        for row in reader:
            print(row['Name'])

def total_inventory_value():
    total_value = 0.0
    with open(file_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            price = float(row['Price'])
            stock = int(row['Stock'])
            total_value += price * stock
    print(f"\nTotal Inventory Value: ${total_value:.2f}")

def low_stock_alert():
    threshold = 10
    low_stock_products = []
    with open(file_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            stock = int(row['Stock'])
            if stock < threshold:
                low_stock_products.append(row)
    if low_stock_products:
        print(f"\n--- Products with Stock Below {threshold} ---")
        for product in low_stock_products:
            print(f"Name: {product['Name']}, Stock: {product['Stock']}")
    else:
        print(f"No products with stock below {threshold}.") 

if __name__ == "__main__":
    main()