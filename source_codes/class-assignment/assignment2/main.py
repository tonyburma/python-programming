class Room:
  def __init__(self, room_number, room_type, price_per_night, is_booked):
    self.room_number = room_number
    self.room_type = room_type
    self.price_per_night = price_per_night
    self.is_booked = is_booked

  def book_room(self):
    if self.is_booked:
      print(f"Room {self.room_number} is already booked.")
    else:
      self.is_booked = True
      print(f"Room {self.room_number} has been booked successfully.")

  def display_status(self):
    status = "Booked" if self.is_booked else "Available"
    
    # status = "Available"
    # if self.is_booked:
    #   status = "Booked"

    print(f"Room {self.room_number} ({self.room_type}): {status}, Price per night: ${self.price_per_night}")

room1 = Room(101, "Single", 100, False)
room2 = Room(102, "Double", 150, True)
room3 = Room(103, "Suite", 300, False)
room4 = Room(104, "Single", 100, False)
room5 = Room(105, "Double", 150, True)
room6 = Room(106, "Suite", 300, False)
rooms = [room1, room2, room3, room4, room5, room6]

def display_menu():
  while True:
    print("1. Display Available Rooms")
    print("2. Display Booked Rooms")
    print("3. Book a Room")
    print("4. Exit")

    choice = input("Enter your choice: ")
    return choice

  

def main():
  while True:
    choice = display_menu()
    
    if choice == '1':
      display_available_rooms()
      
    elif choice == '2':
      display_booked_rooms()
    elif choice == '3':
      room_number = int(input("Enter room number to book: "))
      for room in rooms:
        if room.room_number == room_number:
          room.book_room()
          break
        else:
          print(f"Room {room_number} not found.")
    elif choice == '4':
      print("Exiting the program.")
      break
    else:
      print("Invalid choice. Please try again.")  


def display_available_rooms():
  # Print available rooms
  for room in rooms:
    if not room.is_booked:
      room.display_status()
      print()

def display_booked_rooms():
  # Print booked rooms
  for room in rooms:
    if room.is_booked:
      room.display_status()
      print() 

if __name__ == "__main__":
  main()

 