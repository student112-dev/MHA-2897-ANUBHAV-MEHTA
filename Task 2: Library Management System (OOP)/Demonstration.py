# Importing all required classes from ClassDefinitions.py
from ClassDefinitions import Library, StudentMember, TeacherMember

# Create a library and add books
library = Library()
library.add_book("Python Basics", "ANUBHAV MEHTA")
library.add_book("Data Structures", "ANUBHAV MEHTA")

# Create a student and a teacher member
student = StudentMember("Alice")
teacher = TeacherMember("Mr. Kumar")

# Display the list of books in the library
print("Available Books:")
library.display_books()
print()

# Student tries to borrow books (limit = 2)
student.borrow_book(library.books[0])   # Book 1: Available
student.borrow_book(library.books[1])   # Book 2: Available
student.borrow_book(library.books[0])   # Exceeds limit – should fail

print()

# Teacher tries to borrow a book that is already borrowed by the student
teacher.borrow_book(library.books[1])   # Not available – should fail
