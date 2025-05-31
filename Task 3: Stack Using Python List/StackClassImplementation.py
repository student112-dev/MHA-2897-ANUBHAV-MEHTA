# Stack class using Python list
# Demonstrates a basic implementation of the stack (LIFO) data structure

class Stack:
    def __init__(self):
        # Initialize an empty list to represent the stack
        self.items = []

    def push(self, item):
        # Add an item to the top of the stack
        self.items.append(item)

    def pop(self):
        # Remove and return the top item if stack is not empty
        return self.items.pop() if not self.is_empty() else None

    def peek(self):
        # Return the top item without removing it
        return self.items[-1] if not self.is_empty() else None

    def is_empty(self):
        # Check if the stack is empty
        return len(self.items) == 0
