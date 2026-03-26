class Car:
  def __init__(self, brand, model, year, is_available):
    self.brand = brand
    self.model = model
    self.year = year
    self.is_available = is_available

  def rent_car(self):
    if self.is_available:
      self.is_available = False
      print(f"You have rented the {self.brand} {self.model}.")
    else:
      print(f"Sorry, the {self.brand} {self.model} is not available for rent.")
  
  def return_car(self):
    if not self.is_available:
      self.is_available = True
      print(f"You have returned the {self.brand} {self.model}.")
    else:
      print(f"The {self.brand} {self.model} was not rented out.")
  
  def display_info(self):
    availability = "Available" if self.is_available else "Not Available"
    print(f"{self.year} {self.brand} {self.model} - {availability}")

# Creating car instances
car1 = Car("Toyota", "Camry", 2020, True)
car2 = Car("Honda", "Civic", 2019, False)
car3 = Car("Ford", "Mustang", 2021, True)
car4 = Car("Chevrolet", "Impala", 2018, False)
car5 = Car("Tesla", "Model 3", 2022, True)

cars = [car1, car2, car3, car4, car5]

def main():
  while True:
    print("\nCar Rental System")
    print("1. Display Available Cars")
    print("2. Rent a Car")
    print("3. Return a Car")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
      print("\nAvailable Cars:")
      for car in cars:
        if car.is_available:
          car.display_info()
    
    elif choice == '2':
      car_brand = input("Enter the brand of the car you want to rent: ")
      car_model = input("Enter the model of the car you want to rent: ")
      for car in cars:
        if car.brand.lower() == car_brand.lower() and car.model.lower() == car_model.lower():
          car.rent_car()
          break
      else:
        print("Car not found.")
    
    elif choice == '3':
      car_brand = input("Enter the brand of the car you want to return: ")
      car_model = input("Enter the model of the car you want to return: ")
      for car in cars:
        if car.brand.lower() == car_brand.lower() and car.model.lower() == car_model.lower():
          car.return_car()
          break
      else:
        print("Car not found.")
    
    elif choice == '4':
      print("Exiting the system. Goodbye!")
      break
    
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

