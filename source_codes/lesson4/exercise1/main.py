class Book:
    def __init__(self, title, author):
        # Initializing attributes 
        self.title = title
        self.author = author

    def __str__(self):
        # This magic method overrides how the object is printed 
        return f"'{self.title}' by {self.author}"

# Usage
my_book = Book(title="Automate the Boring Stuff with Python", author="Al Sweigart")
# This calls the __str__ method automatically
print(my_book)