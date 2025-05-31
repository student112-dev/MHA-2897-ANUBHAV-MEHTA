# Book class represents each book in the library
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        return f"{self.title} by {self.author} ({'Available' if self.available else 'Not Available'})"

# Base class for all members (Encapsulation with _borrowed_books)
class Member:
    def __init__(self, name):
        self.name = name
        self._borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            self._borrowed_books.append(book)
            book.available = False
            print(f"{self.name} borrowed '{book.title}'")
        else:
            print(f"'{book.title}' is not available.")

    def return_book(self, book):
        if book in self._borrowed_books:
            self._borrowed_books.remove(book)
            book.available = True
            print(f"{self.name} returned '{book.title}'")

# Student inherits from Member (Inheritance)
class StudentMember(Member):
    def borrow_book(self, book):
        if len(self._borrowed_books) >= 2:
            print("Student borrowing limit reached (2 books).")
        else:
            super().borrow_book(book)

# Teacher inherits from Member (Different borrowing limit - Polymorphism)
class TeacherMember(Member):
    def borrow_book(self, book):
        if len(self._borrowed_books) >= 5:
            print("Teacher borrowing limit reached (5 books).")
        else:
            super().borrow_book(book)

# Library class to manage books and members
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))

    def display_books(self):
        for book in self.books:
            print(book)
