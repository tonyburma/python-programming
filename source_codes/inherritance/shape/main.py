class Shape:
  def __init__(self, type):
    self.name = type

  def area(self):
    print("Area method not implemented for base Shape class.")

class Circle(Shape):
  def __init__(self, radius):
    super().__init__("Circle")
    self.radius = radius

  def area(self):
    return 3.14 * self.radius ** 2
  
class Square(Shape):
  def __init__(self, side_length):
    super().__init__("Square")
    self.side_length = side_length

  def area(self):
    return self.side_length ** 2
  
class Rectangle(Shape):
  def __init__(self, width, height):
    super().__init__("Rectangle")
    self.width = width
    self.height = height

  def area(self):
    return self.width * self.height
  
def main():
  circle = Circle(5)
  square = Square(4)
  rectangle = Rectangle(3, 6)

  print(f"{circle.name} area: {circle.area()}")
  print(f"{square.name} area: {square.area()}")
  print(f"{rectangle.name} area: {rectangle.area()}")

if __name__ == "__main__":
  main()