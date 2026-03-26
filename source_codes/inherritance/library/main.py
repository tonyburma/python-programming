class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author
  
  def __str__(self):
    return f"'{self.title}' by {self.author}"


def main():
  book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
  print(book1)

if __name__ == "__main__":
  main()