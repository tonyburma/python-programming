import math

class Shape:
    def area(self):
        # A placeholder method to be overridden by subclasses 
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        # Specific formula for Square
        return self.side ** 2

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        # Specific formula for Circle using math library 
        return math.pi * (self.radius ** 2)

# Demonstration of Polymorphism
shapes = [Square(4), Circle(3)]

for s in shapes:
    # Each object uses its own version of the area() method 
    print(f"The area is: {s.area():.2f}")