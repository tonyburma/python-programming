class Vehicle:
    def __init__(self, license_plate, fuel_level, capacity):
        self.license_plate = license_plate
        self.fuel_level = fuel_level
        self.capacity = capacity

    def calculate_delivery_cost(self, distance):
        # Base rate: $2 per km
        return distance * 2

class Truck(Vehicle):
    def __init__(self, license_plate, fuel_level, capacity, trailer_type):
        super().__init__(license_plate, fuel_level, capacity)
        self.trailer_type = trailer_type

    def calculate_delivery_cost(self, distance):
        # Truck has a heavy load surcharge (Base + $100)
        return (distance * 3.5) + 100

class Motorcycle(Vehicle):
    def calculate_delivery_cost(self, distance):
        # Motorcycle is cheaper per km, no base fee
        return distance * 1.5
    
class Van(Vehicle):
    def __init__(self, license_plate, fuel_level, capacity, is_refrigerated=False):
        super().__init__(license_plate, fuel_level, capacity)
        self.is_refrigerated = is_refrigerated

    def calculate_delivery_cost(self, distance):
        # Van has a moderate rate (Base + $50)
        return (distance * 2.5) + 50

# Polymorphism in action
vehicles = [
    Truck("TNK-1234", 100, 5000, "Flatbed"),
    Motorcycle("YGN-5678", 10, 50),
    Van("VAN-9012", 80, 2000, is_refrigerated=True)
]


for v in vehicles:
    print(f"Vehicle {v.license_plate} cost for 150km: ${v.calculate_delivery_cost(150)}")