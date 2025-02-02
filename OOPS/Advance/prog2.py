class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_borrowed:
                book.is_borrowed = True
                return f"You have borrowed '{title}'."
        return "Book not available."

    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.is_borrowed:
                book.is_borrowed = False
                return f"'{title}' has been returned."
        return "Invalid return request."

# Example Usage
library = Library()
b1 = Book("Python 101", "John Doe")
b2 = Book("OOP in Python", "Jane Smith")

library.add_book(b1)
library.add_book(b2)

print(library.borrow_book("Python 101"))  # Output: You have borrowed 'Python 101'.
print(library.return_book("Python 101"))  # Output: 'Python 101' has been returned.
