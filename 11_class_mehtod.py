"""11. Class Methods
Assignment:
Create a class Book with a class variable total_books. 
Add a class method increment_book_count() to increase the count when a new book is added."""

class Book:
    total_books = 0  # Class variable to keep track of total books
    def __init__(self, title):
        self.title = title
        Book.increment_total_books()
    @classmethod
    def increment_total_books(cls):
        cls.total_books += 1
book1 = Book("python")
book2 = Book("java")
book3 = Book("c++")

print("Total books:", Book.total_books)  # Output: Total books: 3